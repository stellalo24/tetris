import pygame
from settings import *

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.score = 0
        self.level = 1
        self.lines_cleared = 0

    def is_valid_position(self, tetrimino):
        for i in range(4):
            for j in range(4):
                if (i * 4) + j in tetrimino.shape_obj.get_image():
                    if (tetrimino.x + j < 0 or tetrimino.x + j >= self.cols or
                        tetrimino.y + i >= self.rows or
                        self.grid[tetrimino.y + i][tetrimino.x + j] != 0):
                        return False
        return True

    def lock_piece(self, tetrimino):
        for i in range(4):
            for j in range(4):
                if (i * 4) + j in tetrimino.shape_obj.get_image():
                    self.grid[tetrimino.y + i][tetrimino.x + j] = tetrimino.shape_obj.color + 1
        self.clear_lines()

    def clear_lines(self):
        lines_to_clear = []
        for i in range(self.rows):
            if all(self.grid[i]):
                lines_to_clear.append(i)
        for line in lines_to_clear:
            del self.grid[line]
            self.grid.insert(0, [0 for _ in range(self.cols)])
        self.lines_cleared += len(lines_to_clear)
        self.score += len(lines_to_clear) * 100
        self.level = self.lines_cleared // 10 + 1

    def draw(self, screen):
        # Draw the grid cells
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] != 0:
                    pygame.draw.rect(screen, colors[self.grid[i][j] - 1],
                                    (j * CELL, i * CELL, CELL, CELL))
                # Draw cell borders
                pygame.draw.rect(screen, BLACK, 
                               (j * CELL, i * CELL, CELL, CELL), 1)
        
        # Draw the bottom border line of the play area
        bottom_y = self.rows * CELL
        pygame.draw.line(screen, WHITE, (0, bottom_y), (self.cols * CELL, bottom_y), 2) 