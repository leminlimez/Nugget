class PBConfigItem:
    def __init__(self, uuid: str, ext: str):
        self.uuid = uuid
        self.extension = ext
        self.posterId = 0

    def to_dict(self) -> dict:
        return {"uuid": self.uuid, "extension": self.extension}
    
    def to_str(self) -> str:
        return f'{self.uuid}  ({self.extension})'

    @classmethod
    def from_dict(cls, data):
        return cls(uuid=data.get("uuid"), ext=data.get("extension"))