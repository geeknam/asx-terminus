from unittest import TestCase
from asxterminus.ui.table import Table


class TestTable(TestCase):

    def setUp(self):
        self.headers = ['a', 'b']
        self.data = [
            {'a': 'a1', 'b': 'b1'},
        ]
        self.table = Table(self.headers, self.data)

    def test_get_headers(self):
        self.assertEquals(
            self.table.get_headers(), self.headers
        )

    def test_get_tab_size(self):
        self.assertEquals(
            self.table.get_tab_size(),
            {'a': 6, 'b': 6}
        )

    def test_basic_table(self):
        projected = self.table.render()
        expected = [
            [('headers', 'a     '), ('headers', 'b     '), '\n'],
            [('cell', 'a1    '), ('cell', 'b1    '), '\n']
        ]
        self.assertEquals(projected, expected)

