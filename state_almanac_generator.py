"""Functions to generate an almanac of all possible board states.

Collated with the number of ideal moves that state is from a solved state.
"""
import json

from copy import deepcopy

from board import Board, PracticeBoard

set_almanac = {0: {"[[1, 2, 3], [4, 5, 6], [7, 8, 9]]"}, 1: {"[[1, 2, 3], [4, 5, 9], [7, 8, 6]]", "[[1, 2, 3], [4, 5, 6], [7, 9, 8]]"}, 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set(), 10: set(), 11: set(), 12: set(), 13: set(), 14: set(), 15: set(), 16: set(), 17: set(), 18: set(), 19: set(), 20: set(), 21: set(), 22: set(), 23: set(), 24: set(), 25: set(), 26: set(), 27: set(), 28: set(), 29: set(), 30: set(), 31: set(),generator_board = Board()


def generate_unique_states_from_sets(complexity, size=3):
    """Start with a state of complexity n and generates states of complexity n + 1."""
    for state in set_almanac[complexity]:
        board = Board(size)
        board.previous_states = []
        board.state = json.loads(state)
        open_y = 1
        open_x = 1
        for row in board.state:
            if 9 in row:
                open_y += board.state.index(row)
                open_x += row.index(9)

        board.open_cell_coords = (open_x, open_y)

        board._determine_legal_moves(board.open_cell_coords)

        for move in board.legal_moves:
            pboard = PracticeBoard(board.state, board.open_cell_coords, board.size)
            pboard.practice_slide(move)
            if str(pboard.practice_state) in set_almanac[complexity - 1]:
                continue
            set_almanac[complexity + 1].add(str(pboard.practice_state))


if __name__ == "__main__":
    print("0 : 1")
    for i in range(31):
        generate_unique_states_from_sets(i + 1)
        print(str(i + 1) + " : " + str(len(set_almanac[i + 1])))

    with open("state_almanac_data.json") as f:
        state_almanac = json.load(f)

    for i in range(32):
        for state in set_almanac[i]:
            state_almanac.setdefault(str(deepcopy(state)), i)
        with open('state_almanac_data.json', 'w') as file:
            json.dump(state_almanac, file)
