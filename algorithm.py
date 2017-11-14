"""."""

from board import Board, PracticeBoard


def manhattan_distance(board, size=3):
    """Sum up the manhattan distance of all numbers in the board."""
    diff = 0
    for y in range(1, size + 1):
        for x in range(1, size + 1):
            idx = board.state[y][x] - 1
            diff += abs((idx % size + 1, idx / size + 1) - (x, y))
    return diff


def a_star(board):
    """Find a solution path by exploring possible boards based on heuristic value."""
