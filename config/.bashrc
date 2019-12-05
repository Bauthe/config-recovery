#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Colourful ls
alias ls='ls --color=auto'

# Setting up prefix
if [[ "$TERM" != "linux" && "$TERM" != "xterm" ]]
then
    PS1='\[\e[1m\]\[\e[32m\][\[\e[21m\]\[\e[37m\]\u\[\e[1m\]\[\e[32m\]@\h \[\e[39m\]\W\[\e[32m\]]\[\e[39m\]\$ \[\e[0m\]'
else
    PS1='\[\e[1m\]\[\e[32m\][\u@\h \W]\$ \[\e[21m\]\[\e[0m\]'
fi

# Appending personal scripts to $PATH
export PATH="${PATH}:/home/baudouin/.local/bin"

# Ignore duplicates in history
export HISTCONTROL=ignoredups
