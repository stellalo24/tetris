# Tetris

A classic Tetris implementation built with Python and Pygame.

## Description

This is a faithful recreation of the classic Tetris game, featuring all seven standard Tetrimino pieces, line clearing mechanics, and a clean, modern interface. The game runs in a 300x600 pixel window with a 20x20 pixel grid system.

## Demo

![Tetris Gameplay Demo](example.gif)
![Alt text](https://raw.githubusercontent.com/wkrouse/Bringing-My-OCD-Online/Gif/1st.gif)
<img src="https://raw.githubusercontent.com/wkrouse/Bringing-My-OCD-Online/Gif/1st.gif" alt="Description of GIF">
![Alt text](https://github.com/wkrouse/Bringing-My-OCD-Online/blob/main/docs/8952xv.gif?raw=true)

## Features

- Classic Tetris gameplay with all seven Tetrimino pieces (I, O, T, S, Z, J, L)
- Smooth piece movement and rotation
- Line clearing mechanics
- Next piece preview
- Modern, clean interface with a dark theme
- Score tracking
- Game over detection

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/tetris.git
cd tetris
```

2. Install the required dependencies:
```bash
pip install pygame
```

## How to Play

1. Run the game:
```bash
python main.py
```

2. Controls:
- Left Arrow: Move piece left
- Right Arrow: Move piece right
- Down Arrow: Soft drop (move piece down faster)
- Up Arrow: Rotate piece clockwise
- Space: Hard drop (instantly drop piece to bottom)

## Game Rules

- Tetrimino pieces fall from the top of the board
- Clear lines by filling them completely with blocks
- The game ends when a piece cannot be placed at the top of the board
- Each cleared line increases your score
- The game speed remains constant

## Project Structure

- `main.py`: Main game loop and logic
- `settings.py`: Game configuration and constants
- `tetrimino.py`: Tetrimino piece class and movement logic
- `shape.py`: Tetrimino shape definitions
- `board.py`: Game board management and line clearing logic

## License

This project is open source and available under the MIT License.
