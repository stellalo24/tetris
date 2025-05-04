import pygame
import random
from settings import *
from tetrimino import Tetrimino
from board import Board

def main():
    pygame.init()
    # Build a Pygame window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris")
    screen.fill(BLACKGROUD)
    pygame.display.update()

    board = Board(ROWS, COLS)
    current_piece = Tetrimino(ROWS, COLS)
    next_piece = Tetrimino(ROWS, COLS)
    game_over = False
    fall_time = 0
    fall_speed = 0.5  # seconds per fall
    clock = pygame.time.Clock()

    running = True
    while running:
        fall_time += clock.get_rawtime()
        clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.move(-1, 0, board.grid)
                if event.key == pygame.K_RIGHT:
                    current_piece.move(1, 0, board.grid)
                if event.key == pygame.K_DOWN:
                    current_piece.move(0, 1, board.grid)
                if event.key == pygame.K_UP:  # Up arrow for rotation
                    current_piece.rotate(board.grid)
                if event.key == pygame.K_SPACE:  # Space for hard drop
                    while current_piece.move(0, 1, board.grid):
                        pass
                    board.lock_piece(current_piece)
                    current_piece = next_piece
                    next_piece = Tetrimino(ROWS, COLS)
                    if not board.is_valid_position(current_piece):
                        game_over = True
                if event.key == pygame.K_r and game_over:
                    # Reset the game
                    board = Board(ROWS, COLS)
                    current_piece = Tetrimino(ROWS, COLS)
                    next_piece = Tetrimino(ROWS, COLS)
                    game_over = False
                    score = 0
                    fall_time = 0

        # Check for long press of the down key
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            current_piece.move(0, 1, board.grid)

        if not game_over:
            if fall_time >= fall_speed * 1000:
                fall_time = 0
                if not current_piece.move(0, 1, board.grid):
                    board.lock_piece(current_piece)
                    current_piece = next_piece
                    next_piece = Tetrimino(ROWS, COLS)
                    if not board.is_valid_position(current_piece):
                        game_over = True

        # Draw the game board area
        screen.fill(BLACKGROUD)
        board.draw(screen)
        
        # Draw current piece
        for i in range(4):
            for j in range(4):
                if (i * 4) + j in current_piece.shape_obj.get_image():
                    pygame.draw.rect(screen, colors[current_piece.shape_obj.color],
                                    ((current_piece.x + j) * CELL, (current_piece.y + i) * CELL, CELL, CELL))

        # Draw UI area
        ui_rect = pygame.Rect(0, BOARD_HEIGHT, UI_WIDTH, UI_HEIGHT)
        pygame.draw.rect(screen, UI_BACKGROUND, ui_rect)

        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {board.score}', True, WHITE)
        screen.blit(score_text, (20, BOARD_HEIGHT + 20))

        # Draw level
        level_text = font.render(f'Level: {board.level}', True, WHITE)
        screen.blit(level_text, (20, BOARD_HEIGHT + 60))

        # Draw lines cleared
        lines_text = font.render(f'Lines: {board.lines_cleared}', True, WHITE)
        screen.blit(lines_text, (20, BOARD_HEIGHT + 100))

        # Draw next piece preview
        next_text = font.render('Next:', True, WHITE)
        screen.blit(next_text, (20, BOARD_HEIGHT + 140))

        # Draw the next piece preview
        for i in range(4):
            for j in range(4):
                if (i * 4) + j in next_piece.shape_obj.get_image():
                    pygame.draw.rect(screen, colors[next_piece.shape_obj.color],
                                    (40 + j * CELL, BOARD_HEIGHT + 180 + i * CELL, CELL, CELL))

        # Draw game over message and replay option
        if game_over:
            # Create a semi-transparent overlay
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(128)  # 50% transparency
            overlay.fill(BLACK)
            screen.blit(overlay, (0, 0))

            # Draw game over text in the center of the screen
            game_over_font = pygame.font.Font(None, 48)
            game_over_text = game_over_font.render('Game Over', True, WHITE)
            replay_text = font.render('Press R to Replay', True, WHITE)
            
            # Center the text
            game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 20))
            replay_rect = replay_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))
            
            screen.blit(game_over_text, game_over_rect)
            screen.blit(replay_text, replay_rect)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

