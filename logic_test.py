import unittest

rows = 3
cols = 3

def get_live_neighbors(grid, pos):
    directions = [-1, 1, -cols, cols]
    live_neighbors = 0

    for d in directions:
        neighbor_pos = pos + d

        if neighbor_pos < 0 or neighbor_pos >= len(grid):
            continue

        if d == -1 and pos % cols == 0:
            continue
        if d == 1 and pos % cols == cols - 1:
            continue

        if grid[neighbor_pos] > 0:
            live_neighbors += 1

    return live_neighbors

class TestGameFunctions(unittest.TestCase):
    def test_get_live_neighbors_center(self):
        grid = [
            0, 1, 0,
            0, 3, 1,
            0, 0, 0
        ]
        self.assertEqual(get_live_neighbors(grid, 4), 3)

    def test_get_live_neighbors_corner(self):
        grid = [
            3, 1, 0,
            0, 0, 0,
            0, 0, 0
        ]
        self.assertEqual(get_live_neighbors(grid, 0), 1)

    def test_get_live_neighbors_edge(self):
        grid = [
            0, 0, 0,
            1, 3, 1,
            0, 0, 0
        ]
        self.assertEqual(get_live_neighbors(grid, 4), 2)

if __name__ == "__main__":
    unittest.main()
