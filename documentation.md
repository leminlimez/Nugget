# Tendies Files (PosterBoard wallpapers)
Tendies files store the file structure to be restored to PosterBoard.

There are 2 formats for these:
1. Container format: a containing folder has the name "container"
  - This restores directly to the app container inside of /var/mobile/Containers/Applications/PosterBoard.app and will keep that file structure.
  - Descriptor UUIDs and wallpaper IDs will not be randomized using this format.
2. Descriptor format: a containing folder has the name "descriptor" or "descriptors"
  - This restores to descriptors inside the container. Currently, it restores to the 61 folder, but in future versions it may be handled by iOS version if needed in future versions. If the structure also changes, this may be automatically handled by Nugget in future versions.
  - Descriptor UUIDs and wallpaper IDs will be randomized, preventing overlapping.
  - It is recommended to use these if you are restoring descriptors to collections since this will be more future proof. Randomization of IDs is also safer.

# Batter Files (PosterBoard templates)
Batter files are similar to tendies files in that they store the file structure to be restored to PosterBoard. They use the same container/descriptor/descriptors folder format as tendies files. In addition, they also contain a `config.json` file that tells Nugget what the user can customize.

## Format
Every option requires 3 properties:
- `type` - the type of option it is (see the specific option types for the required string)
- `label` - what text will be displayed in Nugget
- `files` - a list of files relative to the parent of the json file

### Identifiers
For Nugget to know what to change inside of .caml files, you can put special identifier tags on the properties that you want to change. To do this, add a `nuggetId` property to the xml tag and set it equal to any valid string (does not have to be a number).

(You will have to modify the file in a text editor to do this.)

It should look something like this:
```xml
<CALayer nuggetId="1" id="#1" allowsEdgeAntialiasing="1" allowsGroupOpacity="1" bounds="0 -28 520 563" contentsFormat="RGBA8" cornerCurve="circular" hidden="0" name="Thing" position="195 365" transform="" zPosition="442">
  <sublayers/>
</CALayer>
```
To use it, just specify the string value in the `identifier` tag of the options you create in `config.json`. The file path should be directly to the .caml file, *not* the .ca file.

If you want to use the default CoreAnimation identifier instead (the one in the "id" tag), then set `use_ca_id` to true in the json.

### Option Types
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
<summary>Set Values</summary>

```json
"type": "set"
```
Properties:
- `identifier` - identifier in xml file (corresponds to nuggetId value)
- `use_ca_id` *(Optional)* - whether or not to use the CoreAnimation id instead of nuggetId
- `key` - the key/tag of the value to change in the property
- `setter_type` - the type of input the user sees for setting the value
  - __Valid types:__ "textbox", "slider", "toggle"
- `min_value` *(Required for slider, optional for others)* - minimum value allowed for input
- `max_value` *(Required for slider, optional for others)* - maximum value allowed for input
- `step` *(Optional, only for slider)* - the interval between each slider value
- `inverted` *(Optional, only for toggle)* - if set to true, values will apply to the file inverted
- `default_value` *(Optional)* - the default value of the input
</details>
<details>
<summary>Remove Files/Values</summary>

```json
"type": "remove"
```
Properties:
- `inverted` *(Optional)* - if set to true, the files will only be deleted if the checkbox is unchecked
- `default_value` *(Optional)* - whether the checkbox starts as true or false (will be false by default)
- `identifier` *(Optional)* - identifier in xml file. Only needed if you are removing a property or layer
- `use_ca_id` *(Optional)* - whether or not to use the CoreAnimation id instead of nuggetId

The `label` property will apply to the checkbox itself.
</details>
<details>
<summary>Files Picker</summary>

```json
"type": "picker"
```
Properties:
- `options` - list of options to show up in the picker. Each option contains a `label` and list of `files`
- `rename` *(Optional)* - whether or not to rename the files chosen by the user
- `names` *(Optional, required if rename is true)* - the list of new names to rename the files to. Must be in the same order as the list of files in the options. Only includes the name of the files, does not need the path.

When the user selects an option from the picker, all other options will be deleted upon applying.
</details>

## Example Config
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
  },

  {
    "type": "picker",
    "label": "Choose Things",
    "rename": true,
    "names": ["background.ca", "foreground.ca"],
    "options": [
      {
        "label": "Option 1",
        "files": ["descriptors/UUID/bg1.ca", "descriptors/UUID/fg1.ca"]
      },
      {
        "label": "Option 2",
        "files": ["descriptors/UUID/bg2.ca", "descriptors/UUID/fg2.ca"]
      },
      {
        "label": "Option 3",
        "files": ["descriptors/UUID/bg3.ca", "descriptors/UUID/fg3.ca"]
      }
    ]
  },

  {
    "type": "remove",
    "label": "Show Object",
    "files": ["descriptors/UUID/version/1/fg.ca/main.caml"],
    "inverted": true,
    "default_value": true,
    "identifier": "1"
  },

  {
    "type": "set",
    "label": "Animation Duration",
    "files": ["descriptors/UUID/version/1/fg.ca/main.caml"],
    "setter_type": "slider",
    "min_value": 0.5,
    "max_value": 3.0,
    "step": 0.1,
    "default_value": 1.0,
    "key": "duration",
    "identifier": "2"
  },
  {
    "type": "set",
    "label": "Flip Geometry",
    "files": ["descriptors/UUID/version/1/fg.ca/main.caml"],
    "setter_type": "toggle",
    "inverted": false,
    "default_value": false,
    "key": "geometryFlipped",
    "identifier": "3"
  }
]
```