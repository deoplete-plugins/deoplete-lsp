--
--------------------------------------------------------------------------------
--         File:  candidates.lua
--------------------------------------------------------------------------------
--

local api = vim.api

local get_candidates = function(_, _, result)
  local success = (result and not vim.tbl_isempty(result)) and true or false
  api.nvim_set_var('deoplete#source#lsp#_results', result)
  api.nvim_set_var('deoplete#source#lsp#_success', success)
  api.nvim_set_var('deoplete#source#lsp#_requested', true)
  api.nvim_call_function('deoplete#auto_complete', {})
end

local request_candidates = function(arguments)
  vim.lsp.buf_request(0, 'textDocument/completion', arguments, get_candidates)
end

return {
  request_candidates = request_candidates
}
