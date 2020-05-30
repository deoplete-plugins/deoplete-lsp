"=============================================================================
" FILE: lsp.vim
" License: MIT license
"=============================================================================

if exists('g:loaded_deoplete_lsp')
  finish
endif

let g:loaded_deoplete_lsp = 1

" Global options definition.
if get(g:, 'deoplete#enable_at_startup', 0)
  call deoplete#lsp#enable()
endif
