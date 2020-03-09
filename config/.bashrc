#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Aliases
alias ls='ls --color=auto'
alias polybar-restart='killall polybar && polybar bottom & disown'
alias config-sync=$HOME/Projects/config-recovery/config-sync

# ex - archive extractor
# usage: ex <file>
ex ()
{
	echo "$1"
  	if [ -f "$1" ] ; then
    	case "$1" in
      		*.tar.bz2)   tar xjf "$1"   ;;
      		*.tar.gz)    tar xzf "$1"   ;;
      		*.bz2)       bunzip2 "$1"   ;;
			*.rar)       unrar x "$1"   ;;
			*.gz)        gunzip "$1"    ;;
			*.tar)       tar xf "$1"    ;;
			*.tbz2)      tar xjf "$1"   ;;
			*.tgz)       tar xzf "$1"   ;;
			*.zip)       unzip "$1"     ;;
			*.Z)         uncompress "$1";;
			*.7z)        7z x "$1"      ;;
			*)           echo "$1 cannot be extracted via ex" ;;
    	esac
  	else
    	echo "$1 is not a valid file"
  	fi
}

# Setting up prefix
if [[ "$TERM" != "linux" && "$TERM" != "xterm" ]]
then
    PS1='\e[1m\][\e[0;37m\]\u\[\e[1;32m\]@\h \[\e[39m\]\W]\$ \[\e[0m\]'
else
    PS1='\[\e[1m\]\[\e[32m\][\u@\h \W]\$ \[\e[21m\]\[\e[0m\]'
fi

# Appending personal scripts to $PATH
export PATH="${PATH}:/home/baudouin/.local/bin"

# Ignore duplicates in history
export HISTCONTROL=ignoredups
