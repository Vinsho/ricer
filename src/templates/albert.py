class AlbertTemplate:
    path = ".config/albert/org.albert.frontend.qmlboxmodel/style_properties.ini"

    template = """[BoxModel]
animation_duration=0
background_color={bg_color}
border_color={fg_color}
border_size=3
cursor_color={fg_color}
font_name=Roboto
foreground_color={fg_color}
highlight_color={alt_fg_color}
icon_size=50
input_color={alt_fg_color}
input_fontsize=25
item_description_fontsize=15
item_title_fontsize=20
max_items=5
padding=4
radius=0
selection_color={alt_bg_color}
settingsbutton_color={alt_fg_color}
settingsbutton_hover_color={fg_color}
settingsbutton_size=16
shadow_color={alt_bg_color}
shadow_size=0
spacing=10
window_width=1000"""
