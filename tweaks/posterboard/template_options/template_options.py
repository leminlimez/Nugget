from enum import Enum
from dataclasses import dataclass
from shutil import rmtree

class OptionType(Enum):
    replace = "replace"
    remove = "remove"
    set = "set"

@dataclass
class TemplateOption:
    type: OptionType
    label: str
    files: list[str]

    def __init__(self, data: dict):
        self.type = OptionType[data['type']]
        self.label = data['label']
        self.files = data['files']

    def apply(self, container_path: str):
        raise NotImplementedError