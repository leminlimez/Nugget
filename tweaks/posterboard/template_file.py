import os
import uuid
import zipfile

from json import load
from typing import Optional

from .tendie_file import TendieFile
from .template_options import OptionType, TemplateOption, ReplaceOption, RemoveOption, SetOption

CURRENT_FORMAT = 1

class TemplateFile(TendieFile):
    options: list[TemplateOption]
    json_path: str

    # TODO: Move these to custom operations
    banner_text: Optional[str] = None # text to go as a banner
    banner_stylesheet: Optional[str] = None # style sheet of the banner
    description: Optional[str] = None # description to go under the file
    format_version: int = CURRENT_FORMAT # format version of config

    def __init__(self, path: str):
        super().__init__(path=path)
        self.options = []
        self.json_path = None

        # find the config.json file
        with zipfile.ZipFile(path, mode="r") as archive:
            for option in archive.namelist():
                if "config.json" in option.lower() and not "descriptor" in option.lower() and not "container" in option.lower():
                    self.json_path = option
                    break
            if self.json_path != None:
                file = archive.open(self.json_path)
                data = load(file)
                # load the options
                if not 'options' in data:
                    raise Exception("No options were found in the config. Make sure that it is in the correct format.")
                self.format_version = int(data['format_version'])
                if self.format_version > CURRENT_FORMAT:
                    raise Exception("This config requires a newer version of Nugget.")
                self.name = f"{data['title']} - by {data['author']}"
                if 'description' in data:
                    self.description = data['description']
                if 'banner_text' in data:
                    self.banner_text = data['banner_text']
                    if 'banner_stylesheet' in data:
                        self.banner_stylesheet = data['banner_stylesheet']

                # TODO: Add error handling
                for option in data['options']:
                    opt_type = OptionType[option['type']]
                    if opt_type == OptionType.replace:
                        self.options.append(ReplaceOption(data=option))
                    elif opt_type == OptionType.remove:
                        self.options.append(RemoveOption(data=option))
                    elif opt_type == OptionType.set:
                        self.options.append(SetOption(data=option))
                    else:
                        raise Exception("Invalid option type in template")
            else:
                raise Exception("No config.json found in file!")
    

    def extract(self, output_dir: str):
        zip_output = os.path.join(output_dir, str(uuid.uuid4()))
        os.makedirs(zip_output)
        with zipfile.ZipFile(self.path, 'r') as zip_ref:
            zip_ref.extractall(zip_output)

        # apply the options
        parent_path = os.path.join(zip_output, os.path.dirname(self.json_path))
        for option in self.options:
            option.apply(container_path=parent_path)