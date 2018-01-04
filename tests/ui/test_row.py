from unittest import TestCase
from asxterminus.ui.table import Row


class TestRow(TestCase):

    def setUp(self):
        self.headers = ['a', 'b']
        self.data = {'a': 'a1', 'b': 'b1'}

    def test_cells(self):
        row = Row(self.headers, self.data, {})
        self.assertEquals(
            row.cells, [('a', 'a1'), ('b', 'b1')]
        )

    def test_render_cell(self):
        row = Row(self.headers, self.data, {})
        rendered = row.render_cell(('a', 'a1'), {})
        self.assertEquals(rendered, ('cell', 'a1             '))

        row = Row(self.headers, self.data, {'a': 4})
        rendered = row.render_cell(('a', 'a1'), {})
        self.assertEquals(rendered, ('cell', 'a1  '))

        row = Row(self.headers, self.data, {'a': 4})
        rendered = row.render_cell(('a', 'a1'), {'a': 'newstyle'})
        self.assertEquals(rendered, ('newstyle', 'a1  '))