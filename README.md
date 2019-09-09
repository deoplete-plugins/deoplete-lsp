# LSP Completion source for deoplete


## Install

* Install LSP enabled neovim
https://github.com/neovim/neovim/pull/10222

* Install the latest deoplete


## Customization

```vim
call lsp#add_server_config('python', { 'execute_path': 'pyls', 'args': [] }, {})
call lsp#add_server_config('rust', { 'execute_path': 'rustup', 'args': ['run', 'stable', 'rls'] }, {})

" For go-langserver
call lsp#add_server_config('go', { 'execute_path': expand('$GOPATH/bin/go-langserver'),
      \ 'args': ['-format-tool', 'gofmt', '-lint-tool', 'golint', '-gocodecompletion']})

" For bingo
" https://github.com/saibing/bingo
call lsp#add_server_config('go', { 'execute_path': 'bingo',
      \ 'args': ['--mode', 'stdio', '--logfile', '/tmp/lspserver.log', '--trace', '--pprof', ':6060']})
```
