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
class MbdbRecord:
    domain: str
    filename: str
    link: str
    hash: bytes
    key: bytes
    mode: _FileMode
    inode: int
    user_id: int
    group_id: int
    mtime: int
    atime: int
    ctime: int
    size: int
    flags: int
    properties: list

    @classmethod
    def from_stream(cls, d: BytesIO):
        #d = BytesIO(data)

        domain_len = int.from_bytes(d.read(2), "big")
        domain = d.read(domain_len).decode("utf-8")

        filename_len = int.from_bytes(d.read(2), "big")
        filename = d.read(filename_len).decode("utf-8")

        link_len = int.from_bytes(d.read(2), "big")
        link = d.read(link_len).decode("utf-8") if link_len != 0xffff else ""

        hash_len = int.from_bytes(d.read(2), "big")
        hash = d.read(hash_len) if hash_len != 0xffff else b""

        key_len = int.from_bytes(d.read(2), "big")
        key = d.read(key_len) if key_len != 0xffff else b""

        mode = _FileMode(int.from_bytes(d.read(2), "big"))
        #unknown2 = int.from_bytes(d.read(4), "big")
        #unknown3 = int.from_bytes(d.read(4), "big")
        inode = int.from_bytes(d.read(8), "big")
        user_id = int.from_bytes(d.read(4), "big")
        group_id = int.from_bytes(d.read(4), "big")
        mtime = int.from_bytes(d.read(4), "big")
        atime = int.from_bytes(d.read(4), "big")
        ctime = int.from_bytes(d.read(4), "big")
        size = int.from_bytes(d.read(8), "big")
        flags = int.from_bytes(d.read(1), "big")

        properties_count = int.from_bytes(d.read(1), "big")
        properties = []

        for _ in range(properties_count):
            name_len = int.from_bytes(d.read(2), "big")
            name = d.read(name_len).decode("utf-8") if name_len != 0xffff else ""

            value_len = int.from_bytes(d.read(2), "big")
            value = d.read(value_len).decode("utf-8") if value_len != 0xffff else ""

            properties.append((name, value))

        return cls(domain, filename, link, hash, key, mode, inode, user_id, group_id, mtime, atime, ctime, size, flags, properties)
    
    def to_bytes(self) -> bytes:
        d = BytesIO()

        d.write(len(self.domain).to_bytes(2, "big"))
        d.write(self.domain.encode("utf-8"))

        d.write(len(self.filename).to_bytes(2, "big"))
        d.write(self.filename.encode("utf-8"))

        d.write(len(self.link).to_bytes(2, "big"))
        d.write(self.link.encode("utf-8"))

        d.write(len(self.hash).to_bytes(2, "big"))
        d.write(self.hash)

        d.write(len(self.key).to_bytes(2, "big"))
        d.write(self.key)

        d.write(self.mode.to_bytes(2, "big"))
        #d.write(self.unknown2.to_bytes(4, "big"))
        #d.write(self.unknown3.to_bytes(4, "big"))
        d.write(self.inode.to_bytes(8, "big"))
        d.write(self.user_id.to_bytes(4, "big"))
        d.write(self.group_id.to_bytes(4, "big"))
        d.write(self.mtime.to_bytes(4, "big"))
        d.write(self.atime.to_bytes(4, "big"))
        d.write(self.ctime.to_bytes(4, "big"))
        d.write(self.size.to_bytes(8, "big"))
        d.write(self.flags.to_bytes(1, "big"))

        d.write(len(self.properties).to_bytes(1, "big"))

        for name, value in self.properties:
            d.write(len(name).to_bytes(2, "big"))
            d.write(name.encode("utf-8"))

            d.write(len(value).to_bytes(2, "big"))
            d.write(value.encode("utf-8"))

        return d.getvalue()
    
@dataclass
class Mbdb:
    records: list[MbdbRecord]

    @classmethod
    def from_bytes(cls, data: bytes):
        d = BytesIO(data)

        if d.read(4) != b"mbdb":
            raise ValueError("Invalid MBDB file")

        if d.read(2) != b"\x05\x00":
            raise ValueError("Invalid MBDB version")

        records = []
        while d.tell() < len(data):
            records.append(MbdbRecord.from_stream(d))

        return cls(records)
    
    def to_bytes(self) -> bytes:
        d = BytesIO()

        d.write(b"mbdb")
        d.write(b"\x05\x00")

        for record in self.records:
            d.write(record.to_bytes())

        return d.getvalue()