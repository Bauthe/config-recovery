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
	Plug 'jdsimcoe/abstract.vim'
	Plug 'zacanger/angr.vim'
	Plug 'nanotech/jellybeans.vim'
	Plug 'danilo-augusto/vim-afterglow'

call plug#end()

" javascript highlighting
let g:javascript_plugin_jsdoc=1

" colorscheme

let g:afterglow_blackout=1
let g:afterglow_italic_comments=1
let g:afterglow_inherit_background=1

let g:jellybeans_overrides = {
\    'background': { 'ctermbg': 'none', '256ctermbg': 'none' },
\}
if has('termguicolors') && &termguicolors
    let g:jellybeans_overrides['background']['guibg'] = 'none'
endif

colorscheme afterglow
