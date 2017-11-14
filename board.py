"""Define the Board and PracticeBoard classes."""

from copy import deepcopy
from random import choice
import json


class PracticeBoard(object):
    """Make an instance of the PracticeBoard class."""

    def __init__(self, state, open_cell_coords, size):
        """Constructor for the PracticeBoard class."""
        self.practice_state = deepcopy(state)
        self.practice_open_cell_coords = open_cell_coords
        self.practice_size = size

    def _practice_tile_at_coords(self, coords):
        """Take in 1-indexed x-y coords and return the tile number there."""
        return self.practice_state[coords[1] - 1][coords[0] - 1]

    def practice_slide(self, coords):
        """Slide the tile at the given coordinates into the open cell."""
        ox, oy = self.practice_open_cell_coords[0] - 1, self.practice_open_cell_coords[1] - 1
        x, y = coords[0] - 1, coords[1] - 1
        self.practice_state[oy][ox], self.practice_state[y][x] = self.practice_state[y][x], self.practice_state[oy][ox]
        self.practice_open_cell_coords = coords

        return self.practice_state

    def determine_legal_moves(self):
        """Fill the list of legal moves."""
        coords = self.practice_open_cell_coords
        legal_moves = []
        up = (coords[0], coords[1] - 1)
        down = (coords[0], coords[1] + 1)
        left = (coords[0] - 1, coords[1])
        right = (coords[0] + 1, coords[1])

        if up[0] > 0 and up[1] > 0 and up[0] <= self.practice_size and up[1] <= self.practice_size:
            legal_moves.append(up)

        if down[0] > 0 and down[1] > 0 and down[0] <= self.practice_size and down[1] <= self.practice_size:
            legal_moves.append(down)

        if left[0] > 0 and left[1] > 0 and left[0] <= self.practice_size and left[1] <= self.practice_size:
            legal_moves.append(left)

        if right[0] > 0 and right[1] > 0 and right[0] <= self.practice_size and right[1] <= self.practice_size:
            legal_moves.append(right)

        return legal_moves


class Board(object):
    """Make an instance of the Board class."""

    def __init__(self, size=3):
        """Constructor for the Board class."""
        self.size = size
        self.previous_states = []
        self.state = []
        self.open_cell_coords = (size, size)
        self.legal_moves = [(size - 1, size), (size, size - 1)]

        num = 1

        for i in range(size):
            row = []

            for j in range(size):
                row.append(num)
                num += 1

            self.state.append(row)
        self.previous_states.append(deepcopy(self.state))

    def _tile_at_coords(self, coords):
        """Take in 1-indexed x-y coords and return the tile number there."""
        x = coords[0] - 1
        y = coords[1] - 1
        return self.state[y][x]

    def slide(self, coords):
        """Slide the tile at the given coordinates into the open cell."""
        self.previous_states.append(self.state)
        ox, oy = self.open_cell_coords[0] - 1, self.open_cell_coords[1] - 1
        x, y = coords[0] - 1, coords[1] - 1
        self.state[oy][ox], self.state[y][x] = self.state[y][x], self.state[oy][ox]
        self.open_cell_coords = coords

        self._determine_legal_moves(coords)

    def _determine_legal_moves(self, coords):
        """Fill the list of legal moves."""
        self.legal_moves = []
        up = (coords[0], coords[1] - 1)
        down = (coords[0], coords[1] + 1)
        left = (coords[0] - 1, coords[1])
        right = (coords[0] + 1, coords[1])

        if up[0] > 0 and up[1] > 0 and up[0] <= self.size and up[1] <= self.size:
            self.legal_moves.append(up)

        if down[0] > 0 and down[1] > 0 and down[0] <= self.size and down[1] <= self.size:
            self.legal_moves.append(down)

        if left[0] > 0 and left[1] > 0 and left[0] <= self.size and left[1] <= self.size:
            self.legal_moves.append(left)

        if right[0] > 0 and right[1] > 0 and right[0] <= self.size and right[1] <= self.size:
            self.legal_moves.append(right)

    def _make_random_move(self):
        """Make a random move. Moves which would result in a previous state are disallowed."""
        invalid_move = True
        while invalid_move:
            check_board = PracticeBoard(self.state, self.open_cell_coords, self.size)

            potential_move = choice(self.legal_moves)

            if check_board.practice_slide(potential_move) in self.previous_states:
                self.legal_moves.remove(potential_move)
            else:
                invalid_move = False

        else:
            self.slide(potential_move)
            self.previous_states.append(deepcopy(self.state))

    def generate_board_states(self, num_of_moves, attempts, size=3):
        """From a solved board, make a number of random moves, and save unique states."""
        dict = {}

        for i in range(attempts):
            board = Board(size)

            for j in range(num_of_moves):
                board._make_random_move()

            dict.setdefault(str(deepcopy(board.state)), num_of_moves)

        return dict

    def solve(self, starting_state):
        """Solve the board, given a starting board state."""
        self.previous_states = []
        self.state = starting_state
        open_y = 1
        open_x = 1
        for row in self.state:
            if 9 in row:
                open_y += self.state.index(row)
                open_x += row.index(9)

        self.open_cell_coords = (open_x, open_y)

        self._determine_legal_moves(self.open_cell_coords)

        with open("state_almanac_data.json") as f:
            state_almanac = json.load(f)

        self.moves_from_solved = state_almanac[str(self.state)]

        while self.moves_from_solved:
            for move in self.legal_moves:
                p_board = PracticeBoard(self.state, self.open_cell_coords, self.size)
                p_board.practice_slide(move)
                if self.moves_from_solved - state_almanac[str(p_board.practice_state)] == 1:
                    self.slide(move)
                    self.moves_from_solved -= 1
                    print(self.state[0])
                    print(self.state[1])
                    print(self.state[2])
                    print("---------")
                    break

        print("Solved!")


if __name__ == "__main__":
    b = Board()
    b.solve([[1, 2, 9], [8, 5, 3], [4, 7, 6]])
