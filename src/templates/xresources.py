class XresourcesTemplate:
    path = ".extend.Xresources"

    template = """
*fading:                15
*fadeColor:             black
*cursorColor:           #16A085
*pointerColorBackground:#2B2C2B
*pointerColorForeground:#16A085

*bg_color: {bg_color}
*fg_color: {fg_color}
*alt_bg_color: {alt_bg_color}
*alt_fg_color: {alt_fg_color}

Xcursor.theme: Breeze
Xcursor.size:  0


! ROFI SETUP HERE !

! Enable the extended coloring options
rofi.color-enabled: true
!                  bg       border   separator
rofi.color-window: *bg_color, #662b37, #662b37
!                  bg       fg       bg-alt   hl-bg    hl-fg
rofi.color-normal: *bg_color, #bfbfbf, #162025, #162025, #662b37
rofi.color-active: #162025, #bfbfbf, #162025, #162025, #662b37
rofi.color-urgent: #162025, #bfbfbf, #162025, #162025, #662b37

rofi.separator-style: solid
rofi.sidebar-mode: false
rofi.lines: 5
!rofi.font: Hack Regular 12
rofi.font: monofur 13
rofi.bw: 1
rofi.columns: 2
rofi.padding: 5
rofi.fixed-num-lines: true
rofi.hide-scrollbar: true
"""
