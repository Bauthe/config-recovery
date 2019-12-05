#!/bin/sh

source ~/.xprofile desktop
xrdb -merge ~/.Xresources
xrandr --output eDP1 --mode 1920x1080 --output HDMI1 --auto --right-of eDP-1-1

exec i3
