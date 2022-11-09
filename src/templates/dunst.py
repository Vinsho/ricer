class DunstTemplate:
    path = ".config/dunst/dunstrc"

    template = """[global]

    monitor = 0

    follow = none

    width = 300

    height = 100

    origin = top-right

    offset = 0x20

    scale = 0

    frame_width = 1

    frame_color = "{fg_color}"

    font = Monospace 8

    format = "<b>%s</b>\n%b"

    alignment = center

    vertical_alignment = center

    icon_theme = Adwaita
    
    icon_position = left

    min_icon_size = 32

    max_icon_size = 75

    icon_path = /usr/share/icons/gnome/16x16/status/:/usr/share/icons/gnome/16x16/devices/

    mouse_left_click = close_current
    mouse_middle_click = do_action, close_current
    mouse_right_click = close_all

[urgency_low]
    background = "{bg_color}"
    foreground = "{alt_fg_color}"
    timeout = 3

[urgency_normal]
    background = "{bg_color}"
    foreground = "{alt_fg_color}"
    timeout = 3

[urgency_critical]
    background = "#900000"
    foreground = "#ffffff"
    frame_color = "#ff0000"
    timeout = 0"""
