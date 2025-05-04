
from settings import *
from shape import Shape

class Tetrimino:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.shape_obj = Shape()
        # Start pieces from the middle top of the board
        self.x = cols // 2 - 2
        self.y = 0

    def intersects(self, board):
        intersects = False
        for i in range(4):
            for j in range(4):
                if (i * 4) + j in self.shape_obj.get_image():
                    if (self.x + j < 0 or self.x + j >= self.cols or
                        self.y + i >= self.rows or
                        (self.y + i >= 0 and board[self.y + i][self.x + j] != 0)):
                        intersects = True
        return intersects

    def move(self, dx, dy, board):
        old_x = self.x
        old_y = self.y
        self.x += dx
        self.y += dy
        if self.intersects(board):
            self.x = old_x
            self.y = old_y
            return False
        return True

    def rotate(self, board):
        old_rotation = self.shape_obj.rotation
        if self.shape_obj.rotate():  # Only try to rotate if the shape can be rotated
            if self.intersects(board):
                # Try moving left or right if rotation causes collision
                for dx in [-1, 1, -2, 2]:
                    self.x += dx
                    if not self.intersects(board):
                        return True
                    self.x -= dx
                # If all adjustments fail, revert rotation
                self.shape_obj.rotation = old_rotation
                return False
            return True
        return False
