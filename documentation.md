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

# Batter Files (Templates)
Batter files are similar to tendies files in that they store the file structure to be restored to a given domain. Nugget will restore the files in the structure of the "Container" folder in your batter file.

For PosterBoard, they use the same container/descriptor/descriptors folder format as tendies files. In addition, they also contain a `config.json` file that tells Nugget what the user can customize.

## Header
Batter files include a header that includes basic information about the batter file.

__Required info:__
- `title` - the title of the operation
- `author` - your name
- `domain` - the domain for where it should be restored to (for PosterBoard, put `AppDomain-com.apple.PosterBoard`)
  - If you want to use sparserestore, make the domain `Sparserestore-<FILEPATH>` (ie `Sparserestore-/var/Managed Preferences`)
- `format_version` - the minimum version of the config format
  - the current version for the latest Nugget update is `"format_version": "1"`
- `options` - a list of user-configurable options (see [Option Format](#option-format) for more info)
  - if you do not want to have any user-configurable options, just use `"options": []`

<details>
<summary>Optional info:</summary>

- `description` - some text info to show under the title

- `min_version` - minimum iOS version supported by the template
- `max_version` - maximum iOS version supported by the template
  - format: `"min_version": "18.0"`
  - you can do just min, just max, none, or both

- `resources` - a list of embedded resources to include (ie banner/preview images, etc)
- `previews` - a list of preview image file names
  - for them to show, their path must be inside of the `resources` list
- `preview_layout` - how the preview images should be laid out (defaults to "horizontal")
  - __Valid types:__ "horizontal", "stacked"

- `banner_text` - some text of a banner
- `banner_stylesheet` - the [Qt style sheet](https://doc.qt.io/qt-6/stylesheet-examples.html) of the banner
</details>

## Option Format
Every option requires 3 properties:
- `type` - the type of option it is (see the specific option types for the required string)
- `label` - what text will be displayed in Nugget
- `files` - a list of files relative to the parent of the json file
- `associated_preview` *(Optional)* - the name of the preview image to associate the option with
  - for certain options, it may apply effects (ie color) or hide the image (ie remove/picker)
  - for picker, this tag must be in each option

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
- `default_value` *(Optional)* - the default value of the input
- `value_type` *(Optional)* - the type of value
  - __Valid types:__ "integer", "float", "string"
- `setter_type` - the type of input the user sees for setting the value
  - __Valid types:__ "textbox", "slider", "toggle", "color_picker"

- Slider Options:
  - `min_value` - minimum value allowed for input
    - *(Required for slider, optional for others)* 
  - `max_value` - maximum value allowed for input
    - *(Required for slider, optional for others)*
  - `step` *(Optional)* - the interval between each slider value

- Toggle Options:
  - `inverted` *(Optional)* - if set to true, values will apply to the file inverted
  - `toggle_off_value` *(Optional)* - the value to set when the toggle is off (for non-boolean values)
  - `toggle_on_value` *(Optional)* - the value to set when the toggle is on

- Color Picker Options:
  - `sets_opacity` *(Optional)* - whether or not opacity is included
    - this will be automatically inferred if you include 4 values in `default_value`
  
__Additional Details:__

The values should be formatted just like they are in the caml. If it is a float, it should still be in quotes in Nugget, i.e. `"1.0"`.

You can add the tag `nuggetOffset` to properties in the caml file and Nugget will offset the user's choice by that value when applying. This tag is formatted like a math equation, with `x` representing the input chosen by the user or `x`, `y`, `z`, and `a` representing multiple values. Example for position:
```xml
<CALayer nuggetId="1" nuggetOffset="(2 * x + 10), (3 * y + 15)" id="#1" allowsEdgeAntialiasing="1" allowsGroupOpacity="1" bounds="0 -28 520 563" contentsFormat="RGBA8" cornerCurve="circular" hidden="0" name="Thing" position="195 365" transform="" zPosition="442">
  <sublayers/>
</CALayer>
```
Each component is separated by a comma. The `nuggetId` property is required in order to use equations.
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
<summary>Picker</summary>

**Note:** This will be implemented in a future version/beta.
```json
"type": "picker"
```
Properties:
- `options` - list of options to show up in the picker. Each option contains a `label` and list of `files`
- `allow_multiple_selection` *(Optional)* - whether or not to let the user choose multiple options
- `rename` *(Optional)* - whether or not to rename the files chosen by the user
  - will not work if `allow_multiple_selection` is `true`
- `names` *(Optional, required if rename is true)* - the list of new names to rename the files to. Must be in the same order as the list of files in the options.
- `default_value` *(Optional)* - the default value to set for the picker based on the index in the array starting from 0 (ex. `"default_value": 0`)
  - when `allow_multiple_selection` is set to true, use `"default_values": [0, 1, 2]`

When the user selects an option from the picker, all other options will be deleted upon applying.
</details>

## Example Config
An example format of `config.json` looks like this:
```json
{
  "title": "My Batter",
  "description": "I love Nugget",
  "author": "lemin",
  "format_version": "1",
  "domain": "AppDomain-com.apple.PosterBoard",
  "options": [
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
      "names": ["descriptors/UUID/background.ca", "descriptors/UUID/foreground.ca"],
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
}
```