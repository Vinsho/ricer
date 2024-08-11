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
        terminal: "rofi-sensible-terminal";
    }}
    """

class RofiScriptTemplate:
    path = 'it/scripts/rofi-brave.sh'
    
    template ="""#!/bin/bash
if [ -z "$1" ]; then
  # Get rows from 'bt list' command
  input=$($HOME/miniconda3/bin/bt list)

  # Split the input into rows
  IFS=$'\\n'
  rows=($input)

  # Function to switch values in a row
  switch_values() {{
    local row="$1"
    local value1
    local value2
    local value3

    IFS=$'\\t' read -r value1 value2 value3 <<<"$row"

    # Switch the values
    switched_row="<span color='{alt_fg_color}'>$value2</span>\\t<span size='smaller' weight='ultralight'>(${{value3:0:50}})\\t$value1</span>"

    echo "$switched_row"
  }}

  # Variable to store the switched rows
  switched_rows=""

  # Process each row and switch values
  for row in "${{rows[@]}}"; do
    switched_row=$(switch_values "$row")
    switched_rows+="$switched_row"$'\\n'
  done
  echo -en "\\0markup-rows\\x1ftrue\\n"
  echo -e "$switched_rows"

else
  last_part=$(echo "$1" | awk -F'[\\t]' '{{print $NF}}')
  
  # If current workspace is not brave, switch to brave
  current_workspace=$($HOME/it/scripts/i3get.sh -r w)
  brave_workspace=$($HOME/it/scripts/i3get.sh -i brave -r w)
  if [ "$current_workspace" != "$brave_workspace" ]; then
    i3-msg workspace $brave_workspace >/dev/null
  fi
  $HOME/miniconda3/bin/bt activate "${{last_part:0:21}}" >/dev/null
fi
"""
