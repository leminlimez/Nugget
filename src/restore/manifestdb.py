import plistlib
import sqlite3
from dataclasses import dataclass
from io import BytesIO

# Mode bitfield
from enum import IntFlag
class _FileMode(IntFlag):
    S_IFMT   = 0o0170000
    S_IFIFO  = 0o0010000
    S_IFCHR  = 0o0020000
    S_IFDIR  = 0o0040000
    S_IFBLK  = 0o0060000
    S_IFREG  = 0o0100000
    S_IFLNK  = 0o0120000
    S_IFSOCK = 0o0140000

    #S_IRWXU  = 0o0000700
    S_IRUSR  = 0o0000400
    S_IWUSR  = 0o0000200
    S_IXUSR  = 0o0000100

    #S_IRWXG  = 0o0000070
    S_IRGRP  = 0o0000040
    S_IWGRP  = 0o0000020
    S_IXGRP  = 0o0000010

    #S_IRWXO  = 0o0000007
    S_IROTH  = 0o0000004
    S_IWOTH  = 0o0000002
    S_IXOTH  = 0o0000001

    S_ISUID  = 0o0004000
    S_ISGID  = 0o0002000
    S_ISVTX  = 0o0001000

@dataclass
class ManifestDBRecord:
    domain: str
    relative_path: str
    file_id: str
    record_flags: int # 1 = file, 2 = directory, 4 = ?
    inode: int
    mode: _FileMode
    user_id: int
    group_id: int
    mtime: int
    atime: int
    ctime: int
    size: int
    flags: int
    protection_class: int

    def generate_plist(self) -> bytes:
        items = {
            'UserID': self.user_id,
            'GroupID': self.group_id,
            'Birth': self.ctime,
            'LastModified': self.mtime,
            'LastStatusChange': self.atime,
            'Size': self.size,
            'Flags': self.flags,
            'Mode': self.mode,
            'InodeNumber': self.inode,
            'ProtectionClass': self.protection_class
        }
        root = {
            '$version': 100000,
            '$objects': [
                '$null', items, self.relative_path,
                {
                    '$classname': 'MBFile',
                    '$classes': ['MBFile', 'NSObject']
                }
            ],
            '$archiver': 'NSKeyedArchiver',
            '$top': {}
        }
        return plistlib.dumps(root, fmt=plistlib.PlistFormat.FMT_BINARY)

@dataclass
class ManifestDB:
    records: list[ManifestDBRecord]

    def write_to(self, out_file: str):
        conn = sqlite3.connect(out_file)
        cursor = conn.cursor()
        # create the database tables
        cursor.execute("CREATE TABLE Files (fileID TEXT PRIMARY KEY, domain TEXT, relativePath TEXT, flags INTEGER, file BLOB)")
        cursor.execute("CREATE TABLE Properties (key TEXT PRIMARY KEY, value BLOB)")
        for record in self.records:
            cursor.execute("INSERT INTO Files (fileID, domain, relativePath, flags, file) VALUES (?, ?, ?, ?, ?)",
                           (record.file_id, record.domain, record.relative_path, record.record_flags, record.generate_plist()))
        conn.commit()
        conn.close()