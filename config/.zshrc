# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
ZSH=/usr/share/oh-my-zsh/

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="bira"

# Uncomment the following line to disable bi-weekly auto-update checks.
DISABLE_AUTO_UPDATE="true"

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS=true

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
HIST_STAMPS="yyyy-mm-dd"

# Which plugins would you like to load?
# Standard plugins can be found in ~/.oh-my-zsh/plugins/*
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git)


# User configuration

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Compilation flags
export ARCHFLAGS="-arch x86_64"

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

#LS colors
. /usr/share/LS_COLORS/dircolors.sh

# End line
ZSH_CACHE_DIR=$HOME/.cache/oh-my-zsh
if [[ ! -d $ZSH_CACHE_DIR ]]; then
	mkdir $ZSH_CACHE_DIR
fi

source $ZSH/oh-my-zsh.sh
