
import random
from settings import colors

class Shape:
    def __init__(self, shape_type=None):
        self.shape_type = shape_type if shape_type is not None else random.randint(0, 6)
        self.color = self.shape_type
        self.rotation = 0
        self.shapes = [
            # I
            [[1, 5, 9, 13], [4, 5, 6, 7]],
            # J
            [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
            # L
            [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
            # O
            [[1, 2, 5, 6]],
            # S
            [[6, 7, 9, 10], [1, 5, 6, 10]],
            # T
            [[1, 4, 5, 6], [1, 5, 6, 9], [4, 5, 6, 9], [1, 4, 5, 9]],
            # Z
            [[4, 5, 9, 10], [2, 6, 5, 9]]
        ]

    def get_image(self):
        return self.shapes[self.shape_type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shapes[self.shape_type])

    



