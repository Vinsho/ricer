class RofiTemplate:
    path = ".config/rofi/config.rasi"

    template = """* {{
        /* Theme settings */
        highlight: bold italic;
        scrollbar: true;

        /* Gruvbox dark colors */
        bg: {bg_color};
        alt-bg: {alt_bg_color};
        fg: {fg_color};
        alt-fg: {alt_fg_color};

        background: @bg;
        border-color: @fg;
        separatorcolor: @alt-bg;

        normal-background: @bg;
        normal-foreground: @fg;
        alternate-normal-background: @bg;
        alternate-normal-foreground: @fg;
        selected-normal-background:  @alt-bg;
        selected-normal-foreground:  @alt-fg;
    }}
    """
