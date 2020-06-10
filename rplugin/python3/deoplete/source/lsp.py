# =============================================================================
# FILE: lsp.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# =============================================================================

import json
from deoplete.source.base import Base


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
    'Reference',
    'Folder',
    'EnumMember',
    'Constant',
    'Struct',
    'Event',
    'Operator',
    'TypeParameter',
]


class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'lsp'
        self.mark = '[lsp]'
        self.rank = 500
        self.input_pattern = r'[^\w\s]$'
        self.is_volatile = True
        self.vars = {}
        self.vim.vars['deoplete#source#lsp#_results'] = []
        self.vim.vars['deoplete#source#lsp#_success'] = False
        self.vim.vars['deoplete#source#lsp#_requested'] = False
        self.vim.vars['deoplete#source#lsp#_prev_input'] = ''

    def gather_candidates(self, context):
        if not self.vim.call('has', 'nvim-0.5.0'):
            return []

        prev_input = self.vim.vars['deoplete#source#lsp#_prev_input']
        if context['input'] == prev_input and self.vim.vars[
                'deoplete#source#lsp#_requested']:
            return self.process_candidates()

        self.vim.vars['deoplete#source#lsp#_requested'] = False
        self.vim.vars['deoplete#source#lsp#_prev_input'] = context['input']

        params = self.vim.call(
            'luaeval',
            'vim.lsp.util.make_position_params()')

        self.vim.call(
            'luaeval', 'require("candidates").request_candidates('
            '_A.arguments)',
            {'arguments': params})

        return []

    def process_candidates(self):
        candidates = []
        results = self.vim.vars['deoplete#source#lsp#_results']
        if not results:
            return
        elif isinstance(results, dict):
            if 'items' not in results:
                self.print_error(
                    'LSP results does not have "items" key:{}'.format(str(results)))
                return
            items = results['items']
        else:
            items = results
        for rec in items:
            if 'textEdit' in rec and rec['textEdit'] is not None:
                textEdit = rec['textEdit']
                if textEdit['range']['start'] == textEdit['range']['end']:
                    previous_input = self.vim.vars['deoplete#source#lsp#_prev_input']
                    new_text = textEdit['newText']
                    word = f'{previous_input}{new_text}'
                else:
                    word = textEdit['newText']
            elif rec.get('insertText', ''):
                if rec.get('insertTextFormat', 1) != 1:
                    word = rec.get('entryName', rec.get('label'))
                else:
                    word = rec['insertText']
            else:
                word = rec.get('entryName', rec.get('label'))

            item = {
                'word': word,
                'abbr': rec['label'],
                'dup': 1,
                'user_data': json.dumps({
                    'lspitem': rec
                })
            }

            if isinstance(rec.get('kind'), int):
                item['kind'] = LSP_KINDS[rec['kind'] - 1]

            if rec.get('detail'):
                item['menu'] = rec['detail']

            if isinstance(rec.get('documentation'), str):
                item['info'] = rec['documentation']
            elif isinstance(rec.get('documentation'), dict) and 'value' in rec['documentation']:
                item['info'] = rec['documentation']['value']

            if rec.get('insertTextFormat') == 2:
                item['kind'] = 'Snippet'

            candidates.append(item)

        return candidates
