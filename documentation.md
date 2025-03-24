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