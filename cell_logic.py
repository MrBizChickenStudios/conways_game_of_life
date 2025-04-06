class Cell_logic:
    def __init__(self):
        pass

    def update(self, cells_pos, rows, cols, cells):
        for i in range(len(cells)):
            live_neighbors = 0
            directions = [-1, 1, -cols, cols, -cols-1, -cols+1, cols-1, cols+1]

            for d in directions:
                neighbor_pos = i + d
                if neighbor_pos < 0 or neighbor_pos >= rows * cols:
                    continue
                if (d in [-1, -cols-1, cols-1] and i % cols == 0) or (d in [1, -cols+1, cols+1] and i % cols == cols - 1):
                    continue
                if cells[neighbor_pos].alive:
                    live_neighbors += 1

            if cells[i].alive:
                cells[i].next_state = live_neighbors in (2, 3)
            else:
                cells[i].next_state = live_neighbors == 3
