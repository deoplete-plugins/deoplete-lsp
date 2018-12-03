# LSP Completion source for deoplete


## Install

* Install LSP enabled neovim
https://github.com/neovim/neovim/pull/6856

* Install the latest deoplete


## Customization

```vim
call lsp#server#add('python', 'pyls')
call lsp#server#add('rust', ['rustup', 'run', 'stable', 'rls'])

" For go-langserver
call lsp#server#add('go', [expand('$GOPATH/bin/go-langserver'),
      \ '-format-tool', 'gofmt', '-lint-tool', 'golint', '-gocodecompletion'])

" For bingo
" https://github.com/saibing/bingo
call lsp#server#add('go', [
      \ 'bingo', '--mode', 'stdio', '--logfile', '/tmp/lspserver.log',
      \ '--trace', '--pprof', ':6060'])
```
