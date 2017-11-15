"""Function to generate an almanac of all possible board states.

States are collated with the number of ideal moves from a solved state.
"""
import json

from copy import deepcopy

from .board import Board, PracticeBoard

set_almanac = {0: {"[[1, 2, 3], [4, 5, 6], [7, 8, 9]]"}}

for i in range(31):
    set_almanac.setdefault(i + 1, set())


def generate_unique_states_from_sets(complexity, size=3):
    """From a state of complexity n, generate all states of complexity n+1."""
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

        pboard = PracticeBoard(board.state)
        for move in board.legal_moves:
            if complexity > 0:
                if str(pboard.practice_slide(move)) in set_almanac[complexity - 1]:
                    continue
            set_almanac[complexity + 1].add(str(pboard.practice_slide(move)))


if __name__ == "__main__":  # pragma: no cover
    for i in range(32):
        generate_unique_states_from_sets(i)
        print(str(i) + " : " + str(len(set_almanac[i])))

    with open("electic_slide/data/state_almanac_data.json") as f:
        state_almanac = json.load(f)

    for i in range(32):
        for state in set_almanac[i]:
            state_almanac.setdefault(str(deepcopy(state)), i)
        with open('electic_slide/data/state_almanac_data.json', 'w') as file:
            json.dump(state_almanac, file)
