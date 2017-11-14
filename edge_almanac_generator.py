"""Functions to generate an almanac of all possible moves, collated with a\
boolean of whether or not the move is ideal."""

from board import Board
from copy import deepcopy
import json


edge_almanac = {}


def generate_edges(num_of_moves, attempts, starting_state, size=3):
    """From a solved board, make a number of random moves, and save unique states."""
    generator_board = Board()
    generator_board.previous_states = []
    generator_board.state = starting_state
    open_y = 1
    open_x = 1
    for row in generator_board.state:
        if 9 in row:
            open_y += generator_board.state.index(row)
            open_x += row.index(9)

    generator_board.open_cell_coords = (open_x, open_y)

    generator_board._determine_legal_moves(generator_board.open_cell_coords)

    for move in generator_board.legal_moves:
        board = Board(size)

        for j in range(num_of_moves):
            board._make_random_move()

        state_almanac.setdefault(str(deepcopy(board.state)), num_of_moves)
        with open('state_almanac_data.json', 'w') as file:
            json.dump(state_almanac, file)


if __name__ == "__main__":

    with open('state_almanac_data.json') as file:
        state_almanac = json.load(file)

    generate_board_states(10, 700000)
    generate_board_states(11, 1000000)
    generate_board_states(12, 1400000)
    generate_board_states(13, 1900000)
    generate_board_states(14, 2500000)

    print(len(state_almanac))