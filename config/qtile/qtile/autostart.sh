#!/bin/bash

### Generic autostarting file ###

# Compositor
picom -b &

# System tray
udiskie --tray &
blueman-applet &
nm-applet &
xfce4-clipman &

# Polkit agent
lxpolkit &