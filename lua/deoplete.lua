--
--------------------------------------------------------------------------------
--         File:  deoplete.lua
--------------------------------------------------------------------------------
--

local get_candidates = function(success, data)
  vim.api.nvim_set_var('deoplete#source#lsp#_results', data)
  vim.api.nvim_set_var('deoplete#source#lsp#_success', success)
  vim.api.nvim_set_var('deoplete#source#lsp#_requested', true)
  vim.api.nvim_call_function('deoplete#auto_complete', {})
end

local request_candidates = function(arguments, filetype)
  vim.lsp.request_async('textDocument/completion',
                               arguments, get_candidates, nil, filetype)
end


return {
  request_candidates = request_candidates
}
