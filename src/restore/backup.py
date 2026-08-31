from dataclasses import dataclass
from datetime import datetime
import plistlib
from pathlib import Path
from base64 import b64decode
from hashlib import sha1
from uuid import uuid4
from . import manifestdb
from .manifestdb import _FileMode
from random import randbytes
from typing import Optional
from os import makedirs
from ..devicemanagement.constants import BackupDevice

import time

# Default nugget file right
# RWX:RX:RX 
DEFAULT = _FileMode.S_IRUSR | _FileMode.S_IWUSR | _FileMode.S_IXUSR | _FileMode.S_IRGRP | _FileMode.S_IXGRP | _FileMode.S_IROTH | _FileMode.S_IXOTH

@dataclass
class BackupFile:
    path: str
    domain: str

    def get_fileID(self) -> bytes:
        return sha1((self.domain + "-" + self.path).encode()).digest()

    def to_record(self) -> manifestdb.ManifestDBRecord:
        raise NotImplementedError()

@dataclass
class ConcreteFile(BackupFile):
    contents: bytes
    src_path: Optional[str] = None
    owner: int = 0
    group: int = 0
    inode: Optional[int] = None
    mode: _FileMode = DEFAULT

    hash: bytes = None
    size: int = None

    def read_contents(self) -> bytes:
        contents = self.contents
        if self.contents == None:
            with open(self.src_path, "rb") as in_file:
                contents = in_file.read()
        # prepopulate hash and size
        self.hash = sha1(contents).digest()
        self.size = len(contents)
        return contents

    def to_record(self) -> manifestdb.ManifestDBRecord:
        if self.inode is None:
            self.inode = int.from_bytes(randbytes(8), "big")
        if self.hash == None or self.size == None:
            self.read_contents()
        return manifestdb.ManifestDBRecord(
            domain=self.domain,
            relative_path=self.path,
            file_id=self.get_fileID().hex(),
            record_flags=1,
            inode=self.inode,
            mode=self.mode | _FileMode.S_IFREG,
            user_id=self.owner,
            group_id=self.group,
            mtime=int(datetime.now().timestamp()),
            atime=int(datetime.now().timestamp()),
            ctime=int(datetime.now().timestamp()),
            size=self.size,
            flags=4,
            protection_class=3
        )

@dataclass
class Directory(BackupFile):
    owner: int = 0
    group: int = 0
    mode: _FileMode = DEFAULT

    def to_record(self) -> manifestdb.ManifestDBRecord:
        return manifestdb.ManifestDBRecord(
            domain=self.domain,
            relative_path=self.path,
            file_id=self.get_fileID().hex(),
            record_flags=2,
            inode=0, # inode is not respected for directories
            mode=self.mode | _FileMode.S_IFDIR,
            user_id=self.owner,
            group_id=self.group,
            mtime=int(datetime.now().timestamp()),
            atime=int(datetime.now().timestamp()),
            ctime=int(datetime.now().timestamp()),
            size=0,
            flags=4,
            protection_class=0
        )
    
@dataclass
class AppBundle:
    identifier: str
    path: str
    container_content_class: str
    version: str = 804

@dataclass
class Backup:
    files: list[BackupFile]
    apps: list[AppBundle]
    device: BackupDevice

    def write_to_directory(self, directory: Path):
        for file in self.files:
            if isinstance(file, ConcreteFile):
                #print("Writing", file.path, "to", directory / sha1((file.domain + "-" + file.path).encode()).digest().hex())
                if file.hash is None:
                    file.read_contents()
                subdir = directory / file.get_fileID().hex()[:2]
                makedirs(subdir, exist_ok=True)
                with open(subdir / file.get_fileID().hex(), "wb") as f:
                    f.write(file.read_contents())
            
        self.generate_manifest_db(directory / "Manifest.db")

        with open(directory / "Status.plist", "wb") as f:
            f.write(self.generate_status())
        
        with open(directory / "Manifest.plist", "wb") as f:
            f.write(self.generate_manifest())

        with open(directory / "Info.plist", "wb") as f:
            f.write(plistlib.dumps(self.device.info))
        

    # def generate_manifest_db(self): # Manifest.mbdb
    #     records = []
    #     for file in self.files:
    #         records.append(file.to_record())
    #     return mbdb.Mbdb(records=records)
    def generate_manifest_db(self, path: str): # Manifest.db
        records = []
        for file in self.files:
            records.append(file.to_record())
        manifestdb.ManifestDB(records=records).write_to(path)
    
    def generate_status(self) -> bytes: # Status.plist
        return plistlib.dumps({
            "BackupState": "new",
            "Date": datetime.fromisoformat("1970-01-01T00:00:00+00:00"),
            "IsFullBackup": False,
            "SnapshotState": "finished",
            "UUID": str(uuid4()).upper(),
            "Version": "3.3"
        })
    
    def generate_manifest(self) -> bytes: # Manifest.plist
        plist = {
            "BackupKeyBag": b64decode("""
    VkVSUwAAAAQAAAAFVFlQRQAAAAQAAAABVVVJRAAAABDud41d1b9NBICR1BH9JfVtSE1D
	SwAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAV1JBUAAA
	AAQAAAAAU0FMVAAAABRY5Ne2bthGQ5rf4O3gikep1e6tZUlURVIAAAAEAAAnEFVVSUQA
	AAAQB7R8awiGR9aba1UuVahGPENMQVMAAAAEAAAAAVdSQVAAAAAEAAAAAktUWVAAAAAE
	AAAAAFdQS1kAAAAoN3kQAJloFg+ukEUY+v5P+dhc/Welw/oucsyS40UBh67ZHef5ZMk9
	UVVVSUQAAAAQgd0cg0hSTgaxR3PVUbcEkUNMQVMAAAAEAAAAAldSQVAAAAAEAAAAAktU
	WVAAAAAEAAAAAFdQS1kAAAAoMiQTXx0SJlyrGJzdKZQ+SfL124w+2Tf/3d1R2i9yNj9z
	ZCHNJhnorVVVSUQAAAAQf7JFQiBOS12JDD7qwKNTSkNMQVMAAAAEAAAAA1dSQVAAAAAE
	AAAAAktUWVAAAAAEAAAAAFdQS1kAAAAoSEelorROJA46ZUdwDHhMKiRguQyqHukotrxh
	jIfqiZ5ESBXX9txi51VVSUQAAAAQfF0G/837QLq01xH9+66vx0NMQVMAAAAEAAAABFdS
	QVAAAAAEAAAAAktUWVAAAAAEAAAAAFdQS1kAAAAol0BvFhd5bu4Hr75XqzNf4g0fMqZA
	ie6OxI+x/pgm6Y95XW17N+ZIDVVVSUQAAAAQimkT2dp1QeadMu1KhJKNTUNMQVMAAAAE
	AAAABVdSQVAAAAAEAAAAA0tUWVAAAAAEAAAAAFdQS1kAAAAo2N2DZarQ6GPoWRgTiy/t
	djKArOqTaH0tPSG9KLbIjGTOcLodhx23xFVVSUQAAAAQQV37JVZHQFiKpoNiGmT6+ENM
	QVMAAAAEAAAABldSQVAAAAAEAAAAA0tUWVAAAAAEAAAAAFdQS1kAAAAofe2QSvDC2cV7
	Etk4fSBbgqDx5ne/z1VHwmJ6NdVrTyWi80Sy869DM1VVSUQAAAAQFzkdH+VgSOmTj3yE
	cfWmMUNMQVMAAAAEAAAAB1dSQVAAAAAEAAAAA0tUWVAAAAAEAAAAAFdQS1kAAAAo7kLY
	PQ/DnHBERGpaz37eyntIX/XzovsS0mpHW3SoHvrb9RBgOB+WblVVSUQAAAAQEBpgKOz9
	Tni8F9kmSXd0sENMQVMAAAAEAAAACFdSQVAAAAAEAAAAA0tUWVAAAAAEAAAAAFdQS1kA
	AAAo5mxVoyNFgPMzphYhm1VG8Fhsin/xX+r6mCd9gByF5SxeolAIT/ICF1VVSUQAAAAQ
	rfKB2uPSQtWh82yx6w4BoUNMQVMAAAAEAAAACVdSQVAAAAAEAAAAA0tUWVAAAAAEAAAA
	AFdQS1kAAAAo5iayZBwcRa1c1MMx7vh6lOYux3oDI/bdxFCW1WHCQR/Ub1MOv+QaYFVV
	SUQAAAAQiLXvK3qvQza/mea5inss/0NMQVMAAAAEAAAACldSQVAAAAAEAAAAA0tUWVAA
	AAAEAAAAAFdQS1kAAAAoD2wHX7KriEe1E31z7SQ7/+AVymcpARMYnQgegtZD0Mq2U55u
	xwNr2FVVSUQAAAAQ/Q9feZxLS++qSe/a4emRRENMQVMAAAAEAAAAC1dSQVAAAAAEAAAA
	A0tUWVAAAAAEAAAAAFdQS1kAAAAocYda2jyYzzSKggRPw/qgh6QPESlkZedgDUKpTr4Z
	Z8FDgd7YoALY1g=="""),
            "Lockdown": self.device.manifest,
            "SystemDomainsVersion": "24.0",
            "Version": "10.0",
            "IsEncrypted": False
        }
        # add the apps
        if len(self.apps) > 0:
            plist["Applications"] = {}
            for app in self.apps:
                appInfo = {
                    "CFBundleIdentifier": app.identifier,
                    "CFBundleVersion": app.version,
                    "ContainerContentClass": app.container_content_class,
                    "Path": app.path
                }
                plist["Applications"][app.identifier] = appInfo
        return plistlib.dumps(plist)