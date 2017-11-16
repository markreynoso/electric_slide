"""Define the Board and PracticeBoard classes."""

from copy import deepcopy
from random import choice


class PracticeBoard(object):
    """Make an instance of the PracticeBoard class."""

    def __init__(self, state):
        """Constructor for the PracticeBoard class."""
        self.practice_state = deepcopy(state)

        flat = [val for row in state for val in row]
        empty = flat.index(9)
        coords = (empty % 3 + 1, empty // 3 + 1)
        self.practice_open_cell_coords = coords
        self.practice_size = len(state)

    def practice_slide(self, coords):
        """Slide the tile at the given coordinates into the open cell."""
        ox, oy = self.practice_open_cell_coords[0] - 1, self.practice_open_cell_coords[1] - 1
        x, y = coords[0] - 1, coords[1] - 1
        practice_copy = deepcopy(self.practice_state)
        practice_copy[oy][ox], practice_copy[y][x] = practice_copy[y][x], practice_copy[oy][ox]

        return practice_copy

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

    def slide(self, coords):
        """Slide the tile at the given coordinates into the open cell."""
        ox, oy = self.open_cell_coords[0] - 1, self.open_cell_coords[1] - 1
        x, y = coords[0] - 1, coords[1] - 1
        self.state[oy][ox], self.state[y][x] = self.state[y][x], self.state[oy][ox]
        self.previous_states.append(deepcopy(self.state))
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
        """Random move. Disallow moves which would result in a previous state."""
        invalid_move = True
        while invalid_move:
            check_board = PracticeBoard(self.state)

            potential_move = choice(self.legal_moves)

            if check_board.practice_slide(potential_move) in self.previous_states:
                self.legal_moves.remove(potential_move)
            else:
                invalid_move = False

        else:
            self.slide(potential_move)
            self.previous_states.append(deepcopy(self.state))

    def solve(self, starting_state, almanac):
        """Solve the board, given a starting board state."""
        state_almanac = almanac
        self.previous_states = [deepcopy(self.state)]
        self.state = starting_state
        open_y = 1
        open_x = 1
        for row in self.state:
            if 9 in row:
                open_y += self.state.index(row)
                open_x += row.index(9)

        self.open_cell_coords = (open_x, open_y)

        self._determine_legal_moves(self.open_cell_coords)

        moves_made = 0

        self.moves_from_solved = state_almanac[str(self.state)]

        while self.moves_from_solved:
            for move in self.legal_moves:
                p_board = PracticeBoard(self.state)
                if self.moves_from_solved - state_almanac[str(p_board.practice_slide(move))] == 1:
                    self.slide(move)
                    self.moves_from_solved -= 1
                    moves_made += 1
                    break

        return moves_made
