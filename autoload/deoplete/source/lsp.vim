"=============================================================================
" FILE: lsp.vim
" AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
" License: MIT license
"=============================================================================

function! deoplete#source#lsp#_handler(success, data) abort
  echomsg string(a:data)
  let g:deoplete#source#lsp#_results[g:deoplete#source#lsp#_id] = a:data
endfunction
