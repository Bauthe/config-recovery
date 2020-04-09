#!/bin/sh

source ~/.xprofile desktop
xrdb -merge ~/.Xresources

exec i3
