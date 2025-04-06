import pygame
import random
from constants import *
import cell_module
import cell_logic

pygame.init()

surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
game_clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

cols, rows = 100, 100
cell_size = GAME_WIDTH // cols

num_cells = cols * rows
grid_list = [0] * num_cells

cell_positions = random.sample(range(num_cells), num_cells // 2)
for pos in cell_positions:
    grid_list[pos] = 1

cells = [cell_module.Cell(pos % cols, pos // cols, cell_size, alive=(pos in cell_positions)) for pos in range(num_cells)]

cell_logic = cell_logic.Cell_logic()

def main():
    running = True
    while running:
        game_clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP and event.key == pygame.K_q:
                running = False
        update()
        draw()
    pygame.quit()

def draw():
    surface.fill((0, 0, 0))
    for row in range(rows):
        for col in range(cols):
            pygame.draw.rect(surface, (169, 169, 169), (col * cell_size, row * cell_size, cell_size, cell_size), 2)
    for cell in cells:
        if cell.alive:
            cell.draw(surface)
    pygame.display.flip()

def update():
    alive_positions = [i for i, cell in enumerate(cells) if cell.alive]
    cell_logic.update(alive_positions, rows, cols, cells)
    for c in cells:
        c.update()

if __name__ == "__main__":
    main()
