"=============================================================================
" FILE: init.vim
" License: MIT license
"=============================================================================

if !exists('s:is_handler_enabled')
  let s:is_handler_enabled = 0
endif

function! deoplete#lsp#init#_is_handler_enabled() abort
  return s:is_handler_enabled
endfunction

function! deoplete#lsp#init#_enable_handler() abort
  call deoplete#lsp#handler#_init()
  let s:is_handler_enabled = 1
endfunction
