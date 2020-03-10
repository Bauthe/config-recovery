#
# ~/.zprofile
#

[[ -f ~/.zshrc ]] && . ~/.zshrc

export PATH=$PATH:$HOME/.local/bin

if systemctl -q is-active graphical.target
then
	[[ ! $DISPLAY && $XDG_VTNR -eq 1 ]] && exec startx
	[[ ! $DISPLAY && $XDG_VTNR -eq 2 ]] && exec nvidia-xrun
fi
