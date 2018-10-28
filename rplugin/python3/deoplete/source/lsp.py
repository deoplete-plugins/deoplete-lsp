# =============================================================================
# FILE: lsp.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# =============================================================================

import time
import re

from .base import Base


class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'lsp'
        self.mark = '[lsp]'
        self.rank = 500
        self.input_pattern = r'\.[a-zA-Z0-9_?!]*|[a-zA-Z]\w*::\w*|->\w*'
        self.vars = {}

    def on_init(self, context):
        self.vim.vars['deoplete#source#lsp#_results'] = {}

    def gather_candidates(self, context):
        if not self.vim.call('exists', '*lsp#server#add'):
            return []

        if not self.vim.call('luaeval',
                             'require("lsp.plugin").client.has_started()'):
            return []

        if context['is_async']:
            return self._async_gather_candidates(context)

        location = {
            'position': {
                'character': context['complete_position'],
                'line': self.vim.call('line', '.') - 1,
            }
        }

        # Todo: Async support does not work!
        # It does not support function name string?
        candidates = self.vim.call(
            'lsp#request_async', 'textDocument/completion',
            location, 'deoplete#source#lsp#_handler')
        self.vim.vars['deoplete#source#lsp#_id'] = str(time.time())
        self.vim.vars['deoplete#source#lsp#_results'] = {}
        context['is_async'] = True
        return []

    def _async_gather_candidates(self, context):
        results = self.vim.vars['deoplete#source#lsp#_results']
        lsp_id = self.vim.vars['deoplete#source#lsp#_id']
        if lsp_id not in results:
            return []

        for candidate in results[lsp_id]:
            word = candidate['word']
            candidate['word'] = re.sub(r'\([^)]*\)', '', word)
            candidate['abbr'] = word
            if isinstance(candidate.get('info', None), str):
                candidate['info'] = re.sub(r'\n.*', '', candidate['info'])
            else:
                candidate['info'] = ''

        return candidates
