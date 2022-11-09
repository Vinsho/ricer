# Arch ricer
Simple way to create and switch themes.

## How to create a new theme
New theme can be created by making a theme from image and saving it:
`ricer -i path/to/image -s theme_name`
or by adding it manually to `config.yaml`

Example:
```
gruv_box_dark:
  bg_color: "#282828"
  alt_bg_color: "#32302f"
  fg_color: "#ebdbb2"
  alt_fg_color: "#6aa29d"
  image_name: cat.jpg
```
- image_name: Name of theme's image. Image needs to be copied to `wallpapers` folder.

## How to load existing theme
Theme added to `config.yaml` can be loaded by:
`ricer -t name_of_theme`

## Tips
Add path to `set_theme.py` to your terminal alias.
