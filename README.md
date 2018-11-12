# LSP Completion source for deoplete


## Install

* Install LSP enabled neovim
https://github.com/neovim/neovim/pull/6856

* Install the latest deoplete


## Customization

```vim
" Use pyls
call lsp#server#add('python', 'pyls')
call lsp#server#add('rust', ['rustup', 'run', 'stable', 'rls'])
```
