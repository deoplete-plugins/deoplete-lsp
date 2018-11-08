--
--------------------------------------------------------------------------------
--         File:  deoplete.lua
--
--        Usage:  ./deoplete.lua
--
--  Description:  
--
--      Options:  ---
-- Requirements:  ---
--         Bugs:  ---
--        Notes:  ---
--       Author:  YOUR NAME (), <>
-- Organization:  
--      Version:  1.0
--      Created:  08/11/18
--     Revision:  ---
--------------------------------------------------------------------------------
--

require('lsp.plugin')

local get_candidates = function(success, data) 
  vim.api.nvim_set_var('deoplete#source#lsp#_results', data)
  vim.api.nvim_set_var('deoplete#source#lsp#_success', success)
  vim.api.nvim_set_var('deoplete#source#lsp#_requested', true)
end

local request_candidates = function(arguments, filetype) 
  vim.lsp.client.request_async('textDocument/completion', arguments, get_candidates, filetype)
end


return {
  request_candidates = request_candidates
}
