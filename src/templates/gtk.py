class GtkTemplate:
    path = ".config/gtk-3.0/gtk.css"

    template = """
label {{color: {fg_color}}}
#clock-button label {{color: {alt_fg_color}}}
"""