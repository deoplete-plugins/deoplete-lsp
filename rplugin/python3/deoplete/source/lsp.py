# =============================================================================
# FILE: lsp.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# =============================================================================

from .base import Base

LSP_KINDS = [
    'Text',
    'Method',
    'Function',
    'Constructor',
    'Field',
    'Variable',
    'Class',
    'Interface',
    'Module',
    'Property',
    'Unit',
    'Value',
    'Enum',
    'Keyword',
    'Snippet',
    'Color',
    'File',
    'Reference'
]


class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'lsp'
        self.mark = '[lsp]'
        self.rank = 500
        self.input_pattern = r'\.[a-zA-Z0-9_?!]*|[a-zA-Z]\w*::\w*|->\w*'
        self.vars = {}
        self.vim.vars['deoplete#source#lsp#_results'] = []
        self.vim.vars['deoplete#source#lsp#_success'] = False
        self.vim.vars['deoplete#source#lsp#_requested'] = False

    def gather_candidates(self, context):
        if not self.vim.call('exists', '*lsp#server#add'):
            return []

        if not self.vim.call('luaeval',
                             'require("lsp.plugin").client.has_started()'):
            return []

        if context['is_async']:
            if self.vim.vars['deoplete#source#lsp#_requested']:
                context['is_async'] = False
                return self.process_candidates()
            return []
        else:
            self.vim.vars['deoplete#source#lsp#_requested'] = False
            context['is_async'] = True

            location = {
                # not working sending the buffer
                # 'textDocument': ''.join(self.vim.current.buffer[:]),
                'position': {
                    'character': context['complete_position'],
                    'line': self.vim.call('line', '.') - 1,
                }
            }

            self.vim.call('luaeval',
                          'require("deoplete").request_candidates(_A.arguments, _A.filetype)',
                          {'arguments': location, 'filetype': context['filetype']})

            return []

    def process_candidates(self):
        completions = []
        for rec in self.vim.vars['deoplete#source#lsp#_results']['items']:
            item = {
                'dup': 0,
            }
            item['word'] = rec.get('entryName', rec.get('label'))
            item['abbr'] = rec['label']

            if 'kind' in rec:
                item['kind'] = LSP_KINDS[rec['kind']]

            if 'detail' in rec:
                item['info'] = rec['detail']

            completions.append(item)

        return completions
