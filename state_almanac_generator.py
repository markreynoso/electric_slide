"""Functions to generate an almanac of all possible board states.

Collated with the number of ideal moves that state is from a solved state.
"""
import json

from copy import deepcopy

from board import Board


generator_board = Board()


state_almanac = {}


def generate_board_states(num_of_moves, attempts, size=3):
    """From solved board, make n random moves, and save unique states."""
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

    for i in range(3):
        generate_board_states(i + 12, ((i + 1) * 300000) + 1200000)

    print(len(state_almanac))
