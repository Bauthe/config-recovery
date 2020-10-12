#!/bin/sh

source ~/.xprofile
xrdb -merge ~/.Xresources

exec qtile
