#!/bin/sh
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed
nm-applet & disown

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh & disown

# Start welcome
/usr/lib/polkit-1/polkitd & disown # start polkit agent from lxsession