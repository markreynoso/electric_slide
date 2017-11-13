"""Functions to generate an almanac of all possible board states, collated with the\
number of ideal moves that state is from a solved state."""

from board import Board
from copy import deepcopy

state_almanac = {
    '[[1, 2, 3], [4, 5, 9], [7, 8, 6]]': 1,
    '[[1, 2, 3], [4, 5, 6], [7, 9, 8]]': 1,

}

generator_board = Board()


def generate_board_states(num_of_moves, attempts, size=3):
    """From a solved board, make a number of random moves, and save unique states."""
    for i in range(attempts):
        board = Board(size)

        for j in range(num_of_moves):
            board._make_random_move()

        state_almanac.setdefault(str(deepcopy(board.state)), num_of_moves)


if __name__ == "__main__":

    for i in range(10):
        generate_board_states(i + 1, (i + 3) ** (i + 2))

        print(len(state_almanac))
