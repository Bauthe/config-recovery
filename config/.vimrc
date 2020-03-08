" Set utf-8
set encoding=utf-8
set fileencoding=utf-8

" Activate the mouse
set mouse=a

" Clipboard
set clipboard=unnamed

" Set good indent
set ts=4 sw=4
filetype indent plugin on

" Search highlighting
set hls is

" Syntax highlighting
syntax on

" Lines numbers
set number

" Nice cursor
set cursorbind

" Useful plugins
call plug#begin('~/.vim/plugged')

	" Make sure you use single quotes
	Plug 'pangloss/vim-javascript'

call plug#end()

" javascript highlighting
let g:javascript_plugin_jsdoc=1
