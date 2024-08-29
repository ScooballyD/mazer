import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )

    def test_maze_create_cells_large(self):
        num_cols = 24
        num_rows = 15

        m1 = Maze(0, 0, num_rows, num_cols, 5, 5, None)
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )

    def test_entrance(self):
        num_cols = 12
        num_rows = 10

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertFalse(m1._cells[0][0].has_top_wall)

    def test_exit(self):
        num_cols = 12
        num_rows = 10

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertFalse(m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall)

    def test_reset(self):
        num_cols = 12
        num_rows = 10

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertFalse(m1._cells[6][5].visited)
        self.assertFalse(m1._cells[11][2].visited)


if __name__ == "__main__":
    unittest.main()
