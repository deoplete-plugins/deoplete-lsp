# =============================================================================
# FILE: lsp.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# =============================================================================

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

    def gather_candidates(self, context):
        if not self.vim.call('exists', '*lsp#server#add'):
            return []

        if not self.vim.call('luaeval',
                             'require("lsp.plugin").client.has_started()'):
            return []

        location = {
            'position': {
                'character': context['complete_position'],
                'line': self.vim.call('line', '.') - 1,
            }
        }

        # Todo: Async support
        candidates = self.vim.call(
            'lsp#request', 'textDocument/completion', location)

        for candidate in candidates:
            word = candidate['word']
            candidate['word'] = re.sub(r'\([^)]*\)', '', word)
            candidate['abbr'] = word
            if isinstance(candidate.get('info', None), str):
                candidate['info'] = re.sub(r'\n.*', '', candidate['info'])
            else:
                candidate['info'] = ''

        return candidates
