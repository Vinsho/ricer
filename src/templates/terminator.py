class TerminatorTemplate:
    path = ".config/terminator/config"

    template = """[global_config]
  cell_height = 1.1
[keybindings]
[profiles]
  [[default]]
    background_color = "{bg_color}"
    background_darkness = 0.95
    background_type = transparent
    cursor_shape = ibeam
    cursor_fg_color = "#1c3535"
    cursor_bg_color = "#c4bc77"
    cursor_color_default = FalsAre you sure?e
    foreground_color = "{fg_color}"
    use_system_font = False
    font = JetBrainsMono Nerd Font Light 9
    show_titlebar = False
    show_scrollbar = False
    scrollback_infinite = True
     palette = "#2e3436:#cc0000:#4e9a06:#c4a000:{alt_fg_color}:#75507b:#06989a:#d3d7cf:#555753:#ef2929:#8ae234:#fce94f:#729fcf:#ad7fa8:#34e2e2:#eeeeec"
[layouts]
  [[default]]
    [[[window0]]]
      type = Window
      parent = ""
    [[[child1]]]
      type = Terminal
      parent = window0
[plugins]
"""
