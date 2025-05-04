import pygame

# Window dimensions
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
BOARD_WIDTH = 300
BOARD_HEIGHT = 500
UI_WIDTH = BOARD_WIDTH
UI_HEIGHT = WINDOW_HEIGHT - BOARD_HEIGHT

# Game board settings
CELL = 20
ROWS = BOARD_HEIGHT // CELL
COLS = BOARD_WIDTH // CELL

# Create the window
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLACKGROUD = (36, 36, 36)
UI_BACKGROUND = (50, 50, 50)

# Tetrimino colors
colors = [
    (0, 255, 255),  # I-Tetrimino (Cyan)
    (255, 255, 0),  # O-Tetrimino (Yellow)
    (128, 0, 128),  # T-Tetrimino (Purple)
    (0, 255, 0),    # S-Tetrimino (Green)
    (255, 0, 0),    # Z-Tetrimino (Red)
    (0, 0, 255),    # J-Tetrimino (Blue)
    (255, 165, 0)   # L-Tetrimino (Orange)
] 