# Documentation
## Tendies Files (PosterBoard wallpapers)
Tendies files store the file structure to be restored to PosterBoard.

There are 2 formats for these:
1. Container format: a containing folder has the name "container"
  - This restores directly to the app container inside of /var/mobile/Containers/Applications/PosterBoard.app and will keep that file structure.
  - Descriptor UUIDs and wallpaper IDs will not be randomized using this format.
2. Descriptor format: a containing folder has the name "descriptor" or "descriptors"
  - This restores to descriptors inside the container. Currently, it restores to the 61 folder, but in future versions it may be handled by iOS version if needed in future versions. If the structure also changes, this may be automatically handled by Nugget in future versions.
  - Descriptor UUIDs and wallpaper IDs will be randomized, preventing overlapping.
  - It is recommended to use these if you are restoring descriptors to collections since this will be more future proof. Randomization of IDs is also safer.

## Batter Files (PosterBoard templates)
Batter files are similar to tendies files in that they store the file structure to be restored to PosterBoard. They use the same container/descriptor/descriptors folder format as tendies files. In addition, they also contain a `config.json` file that tells Nugget what the user can customize.

An example format of `config.json` looks like this:
```json
[
  {
    "type": "replace",
    "label": "Background Image",
    "button_label": "Select Image",
    "allowed_files": "Image Files (*.png)",
    "required": true,
    "files": ["descriptors/UUID/version/1/bg/assets/image.png", "descriptors/UUID/version/1/fg/assets/image2.png"]
  },
  {
    "type": "remove",
    "label": "File Thing Visible",
    "files": ["descriptors/UUID2/version/1/bg/assets/file1.png"]
  },
  {
    "type": "remove",
    "label": "Include collection item",
    "files": ["descriptors/UUID3"],
    "inverted": true,
    "default_value": true
  }
]
```

### Format + Option Types
Every option requires 3 properties:
- `type` - the type of option it is (see the specific option types for the required string)
- `label` - what text will be displayed in Nugget
- `files` - a list of files relative to the parent of the json file

<details>
<summary>Replace Files</summary>

```json
"type": "replace"
```
Properties:
- `button_label` *(Optional)* - what text to display on the import button
- `allowed_files` - the types of files and allowed extensions (follows the [QT filter format](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QFileDialog.html#PySide6.QtWidgets.QFileDialog.setNameFilter))
- `required` - whether or not the user must select a file in order for the template to apply
</details>
<details>
<summary>Remove Files</summary>

```json
"type": "remove"
```
Properties:
- `inverted` *(Optional)* - if set to true, the files will only be deleted if the checkbox is unchecked
- `default_value` *(Optional)* - whether the checkbox starts as true or false (will be false by default)

The `label` property will apply to the checkbox itself.
</details>