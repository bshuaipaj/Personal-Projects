# Minimax Algorithm for Tic-Tac-Toe

## Description

This program implements the Minimax algorithm for Tic-Tac-Toe, written in Python. The program takes three command line arguments to determine the algorithm to use, who begins the game, and the mode of the game.

## Command Line Arguments

The program requires three arguments:
1. **ALGO**: Specifies which algorithm the computer player will use.
2. **FIRST**: Specifies who begins the game.
3. **MODE**: Specifies the mode in which the program should operate.

### Argument Details

- **ALGO**: Algorithm used by the computer player:
  - `1`: MiniMax
  - `2`: MiniMax with alpha-beta pruning

- **FIRST**: Specifies the player who makes the first move:
  - `X`: Player X (human or computer)
  - `O`: Player O (human or computer)

- **MODE**: Game mode that determines who plays:
  - `1`: Human (X) vs. Computer (O)
  - `2`: Computer (X) vs. Computer (O)

## Usage Example

To run the program from the command line, you would use a format like:

```bash
python tictactoe.py 1 X 1
