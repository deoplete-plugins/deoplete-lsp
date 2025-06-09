# LSP Completion source for deoplete

**Note**: The development of this plugin is finished. Accepts minor patches and
issues but no new features.  And the plugin does not support the latest
nvim-lsp specification.

[ddc.vim](https://github.com/Shougo/ddc.vim) with
[ddc-source-lsp](https://github.com/Shougo/ddc-source-lsp) is the next
generation auto completion plugin. Consider migrating to it.


## Install

- Install LSP enabled [neovim](https://github.com/neovim/neovim)(version 0.5.0+)

- Install the latest [deoplete](https://github.com/Shougo/deoplete.nvim)

- Install and configure [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig)

## Configuration

- `g:deoplete#lsp#handler_enabled`: If you set it to v:true, you can disable
  hover handler.

- `g:deoplete#lsp#use_icons_for_candidates`: Set to v:true to enable icons for
  LSP candidates. Requires patched font: https://www.nerdfonts.com/
