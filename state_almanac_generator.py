"""Functions to generate an almanac of all possible board states, collated with the\
number of ideal moves that state is from a solved state."""

from board import Board
from copy import deepcopy
import json


generator_board = Board()


state_almanac = {}


def generate_board_states(num_of_moves, attempts, size=3):
    """From a solved board, make a number of random moves, and save unique states."""
    for i in range(attempts):
        board = Board(size)

        for j in range(num_of_moves):
            board._make_random_move()

        state_almanac.setdefault(str(deepcopy(board.state)), num_of_moves)
        with open('state_almanac_data.json', 'w') as file:
            json.dump(state_almanac, file)


if __name__ == "__main__":

    with open('state_almanac_data.json') as file:
        state_almanac = json.load(file)

    # for i in range(1):
    generate_board_states(8, 300000)

    print(len(state_almanac))
