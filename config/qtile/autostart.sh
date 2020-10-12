#!/bin/bash

################################
### Autostart file for qtile ###
################################

### Compositor ###
picom -b &

### Background session utilities ###

#clipman is started only if it was not running already
pgrep xfce4-clipman || xfce4-clipman &
lxpolkit &
/lib/xfce4/notifyd/xfce4-notifyd &

### System tray ###
blueman-applet &
nm-applet &
