"""."""

from board import Board, PracticeBoard


def manhattan_distance(board):
    """Sum up the manhattan distance of all numbers in the board."""
    actual_coords = actual_coordinates()
    diff = 0
    for y in range(1, 4):
        for x in range(1, 4):
            diff += abs(actual_coords[board.state[y][x]] - (x, y))


def actual_coordinates():
    """Create a dictionary of coordinates where each tile value should be."""
    actual_coords = {}
    actual_coords[1] = (1, 1)
    actual_coords[2] = (2, 1)
    actual_coords[3] = (3, 1)
    actual_coords[4] = (1, 2)
    actual_coords[5] = (2, 2)
    actual_coords[6] = (3, 2)
    actual_coords[7] = (1, 3)
    actual_coords[8] = (2, 3)
    actual_coords[9] = (3, 3)
    return actual_coords


def a_star(board):
    """Find a solution path by exploring possible boards based on heuristic value."""
