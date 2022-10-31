# LSP Completion source for deoplete

## Install

- Install LSP enabled [neovim](https://github.com/neovim/neovim)(version 0.5.0+)

- Install the latest [deoplete](https://github.com/Shougo/deoplete.nvim)

- Install and configure [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig)

## Configuration

- `g:deoplete#lsp#handler_enabled`: If you set it to v:true, you can disable
  hover handler.

- `g:deoplete#lsp#use_icons_for_candidates`: Set to v:true to enable icons for
  LSP candidates. Requires patched font: https://www.nerdfonts.com/
