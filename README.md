# :rice: Arch ricer 
Simple way to create and switch themes.

## How to create a new theme

### Create theme from an existing image
New theme can be created by making a theme from image:

`ricer -i path/to/image -s theme_name`

Image can be anywhere in your pc, it will be copied to wallpapers folder + theme will be added automatically to config.yaml for later use.

### Create theme manually
You can create theme manually by adding palette and image_name to `config.yaml`.

Example:
```
gruv_box_dark:
  bg_color: "#282828"
  alt_bg_color: "#32302f"
  fg_color: "#ebdbb2"
  alt_fg_color: "#6aa29d"
  image_name: cat.jpg
```
- `image_name`: Name of theme's image. Image needs to be copied to `wallpapers` folder.

## How to load existing theme
Theme added to `config.yaml` can be loaded by:
`ricer -t name_of_theme`

## Tips
Add path to `set_theme.py` to your terminal alias.
