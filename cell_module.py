import pygame

class Cell:
    def __init__(self, x, y, size, alive=False):
        self.x = x
        self.y = y
        self.size = size
        self.alive = alive
        self.next_state = alive

    def draw(self, surface):
        if self.alive:
            pygame.draw.rect(
                surface,
                (0, 255, 0),
                (self.x * self.size, self.y * self.size, self.size, self.size)
            )

    def update(self):
        self.alive = self.next_state
