# if type "xrandr"; then
#   for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
#     MONITOR=$m polybar --reload main_bar &
#   done
# else
#   polybar --reload main_bar &

#!/usr/bin/env sh
killall -q polybar

# Wait until processes have been shut down
# while grep -x polybar >/dev/null; do sleep 1; done

polybar & > /dev/null;
