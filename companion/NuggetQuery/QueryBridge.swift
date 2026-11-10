import Foundation
import Darwin

struct QueryRequest: Codable {
    let protocolVersion: Int
    let id: String
    let build: String
    let version: String
    let operation: String
    let contents: Data

    enum CodingKeys: String, CodingKey {
        case protocolVersion = "protocol"
        case id, build, version, operation, contents
    }
}

struct QueryResult: Codable {
    let protocolVersion = 1
    let id: String
    let build: String
    let success: Bool
    let message: String

    enum CodingKeys: String, CodingKey {
        case protocolVersion = "protocol"
        case id, build, success, message
    }
}

struct OriginalBackup: Codable {
    let build: String
    let contents: Data
}

enum QueryError: LocalizedError {
    case message(String)
    var errorDescription: String? {
        if case .message(let message) = self { return message }
        return nil
    }
}

/// Deliberately limited to the MobileGestalt container. Requests cannot supply paths.
enum QueryBridge {
    static let files = FileManager.default
    static let documents = files.urls(for: .documentDirectory, in: .userDomainMask)[0]
    static let pending = documents.appendingPathComponent("NuggetQuery-pending.plist")
    static let processing = documents.appendingPathComponent("NuggetQuery-processing.plist")
    static let result = documents.appendingPathComponent("NuggetQuery-result.plist")
    static let container = "/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache"
    static let target = URL(fileURLWithPath: container + "/Library/Caches/com.apple.MobileGestalt.plist")

    static func currentBuild() throws -> String {
        var size = 0
        guard sysctlbyname("kern.osversion", nil, &size, nil, 0) == 0, size > 0 else {
            throw QueryError.message("Could not determine the system build.")
        }
        var value = [CChar](repeating: 0, count: size)
        guard sysctlbyname("kern.osversion", &value, &size, nil, 0) == 0 else {
            throw QueryError.message("Could not read the system build.")
        }
        return String(cString: value)
    }

    static func validateOS() throws {
        let os = ProcessInfo.processInfo.operatingSystemVersion
        guard os.majorVersion == 27, os.minorVersion < 2 || (os.minorVersion == 2 && os.patchVersion == 0) else {
            throw QueryError.message("This experimental bridge supports iOS 27.0–27.2 only.")
        }
    }

    static func validatePlist(_ data: Data) throws {
        let plist = try PropertyListSerialization.propertyList(from: data, options: [], format: nil)
        guard let root = plist as? [String: Any], root["CacheExtra"] is [String: Any] else {
            throw QueryError.message("This is not a MobileGestalt plist (CacheExtra is missing).")
        }
    }

    static func load() throws -> QueryRequest {
        try validateOS()
        guard !files.fileExists(atPath: processing.path) else {
            throw QueryError.message("An interrupted request exists. Check the file before discarding it and retrying.")
        }
        let request = try PropertyListDecoder().decode(QueryRequest.self, from: Data(contentsOf: pending))
        guard request.protocolVersion == 1, UUID(uuidString: request.id) != nil,
              request.build == (try currentBuild()) else {
            throw QueryError.message("Request protocol or system build does not match this device.")
        }
        let os = ProcessInfo.processInfo.operatingSystemVersion
        let parts = request.version.split(separator: ".").compactMap { Int($0) }
        guard !parts.isEmpty, parts.count <= 3,
              parts + Array(repeating: 0, count: 3 - parts.count) == [os.majorVersion, os.minorVersion, os.patchVersion] else {
            throw QueryError.message("Request system version does not match this device.")
        }
        guard request.operation == "write" || request.operation == "restore_original" else {
            throw QueryError.message("Unsupported operation.")
        }
        if request.operation == "write" { try validatePlist(request.contents) }
        return request
    }

    static func withAccess<T>(_ body: () throws -> T) throws -> T {
        try validateOS()
        guard let group = Bundle.main.object(forInfoDictionaryKey: "NuggetQueryAppGroup") as? String,
              !group.isEmpty else {
            throw QueryError.message("NuggetQueryAppGroup is not configured.")
        }
        let handle = worse_query(container, group, false, false)
        guard handle >= 0 else {
            throw QueryError.message("worse_query failed (\(handle)). Check App Group signing and OS compatibility.")
        }
        defer { worse_query_release(handle) }
        return try body()
    }

    static func writeInPlace(_ data: Data) throws {
        // Preserve the existing file's inode, owner and permissions.
        let handle = try FileHandle(forWritingTo: target)
        defer { try? handle.close() }
        try handle.seek(toOffset: 0)
        try handle.write(contentsOf: data)
        try handle.truncate(atOffset: UInt64(data.count))
        try handle.synchronize()
        guard try Data(contentsOf: target) == data else {
            throw QueryError.message("MobileGestalt read-back verification failed.")
        }
    }

    static func update(_ request: QueryRequest) throws {
        try withAccess {
            let original = try Data(contentsOf: target)
            try validatePlist(original)
            let backupURL = documents.appendingPathComponent("MobileGestalt-original-\(request.build).plist")
            var replacement = request.contents
            if request.operation == "restore_original" {
                let backup = try PropertyListDecoder().decode(OriginalBackup.self, from: Data(contentsOf: backupURL))
                guard backup.build == request.build else { throw QueryError.message("Backup build mismatch.") }
                replacement = backup.contents
            } else if !files.fileExists(atPath: backupURL.path) {
                // Save once per OS build. Later writes must never replace the original backup.
                let backup = OriginalBackup(build: request.build, contents: original)
                try PropertyListEncoder().encode(backup).write(to: backupURL, options: .atomic)
            }
            try validatePlist(replacement)
            do {
                try writeInPlace(replacement)
            } catch {
                let writeError = error.localizedDescription
                do { try writeInPlace(original) }
                catch {
                    throw QueryError.message("Write failed: \(writeError). Rollback also failed: \(error.localizedDescription). Original backup remains in Documents.")
                }
                throw QueryError.message("Write failed; previous contents restored: \(writeError)")
            }
        }
    }

    static func apply(_ displayed: QueryRequest) throws -> String {
        // Re-read after preview so an old preview cannot apply a different request.
        let request = try load()
        guard request.id == displayed.id, request.contents == displayed.contents,
              request.operation == displayed.operation else {
            throw QueryError.message("The request changed. Load it again before applying.")
        }
        try files.moveItem(at: pending, to: processing)
        let outcome: QueryResult
        do {
            try update(request)
            outcome = QueryResult(id: request.id, build: request.build, success: true,
                                  message: "MobileGestalt verified. Restart the device to see changes.")
        } catch {
            outcome = QueryResult(id: request.id, build: request.build, success: false,
                                  message: error.localizedDescription)
        }
        // Publish result before removing the processing marker. A crash cannot look successful.
        try PropertyListEncoder().encode(outcome).write(to: result, options: .atomic)
        try files.removeItem(at: processing)
        if !outcome.success { throw QueryError.message(outcome.message) }
        return outcome.message
    }

    static func discard() throws {
        for url in [pending, processing] where files.fileExists(atPath: url.path) {
            let request = try PropertyListDecoder().decode(QueryRequest.self, from: Data(contentsOf: url))
            let outcome = QueryResult(id: request.id, build: request.build, success: false,
                                      message: "Request discarded in NuggetQuery. Check the current file before retrying.")
            try PropertyListEncoder().encode(outcome).write(to: result, options: .atomic)
            try files.removeItem(at: url)
        }
    }

    static func exportCurrent() throws -> URL {
        try withAccess {
            let data = try Data(contentsOf: target)
            try validatePlist(data)
            let url = documents.appendingPathComponent("com.apple.MobileGestalt.plist")
            try data.write(to: url, options: .atomic)
            return url
        }
    }
}
