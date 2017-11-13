"""Define the Board and Cell classes."""

# from random import randint
from random import choice


class PracticeBoard(object):
    """Make an instance of the PracticeBoard class."""

    def __init__(self, state, open_cell_coords, size):
        """Constructor for the PracticeBoard class."""
        self.practice_state = state
        self.practice_open_cell_coords = open_cell_coords
        self.practice_size = size

    def _practice_tile_at_coords(self, coords):
        """Take in 1-indexed x-y coords and return the tile number there."""
        return self.practice_state[coords[1] - 1][coords[0] - 1]

    def practice_slide(self, coords):
        """Slide the tile at the given coordinates into the open cell."""
        tile_to_move = self._practice_tile_at_coords(coords)
        self.practice_state[coords[1] - 1][coords[0] - 1] = self.practice_size ** 2
        self.practice_state[self.practice_open_cell_coords[1] - 1][self.practice_open_cell_coords[0] - 1] = tile_to_move
        self.practice_open_cell_coords = coords

        return self.practice_state


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

    def _tile_at_coords(self, coords):
        """Take in 1-indexed x-y coords and return the tile number there."""
        x = coords[0] - 1
        y = coords[1] - 1
        return self.state[y][x]

    def slide(self, coords):
        """Slide the tile at the given coordinates into the open cell."""
        print(self.state)
        self.previous_states.append(self.state)
        tile_to_move = coords[0] + self.size * (coords[1] - 1)
        self.state[self.open_cell_coords[1] - 1][self.open_cell_coords[0] - 1] = tile_to_move
        self.state[coords[1] - 1][coords[0] - 1] = self.size ** 2
        self.open_cell_coords = coords
        print(self.state)

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
        check_board = PracticeBoard(self.state, self.open_cell_coords, self.size)

        # potential_move = self.legal_moves[randint(0, len(self.legal_moves) - 1)]

        potential_move = choice(self.legal_moves)

        if check_board.practice_slide(potential_move) in self.previous_states:
            self.legal_moves.remove(potential_move)
            self._make_random_move()

        else:
            self.slide(potential_move)


def generate_board_states(num_of_moves, attempts, size=3):
    """From a solved board, make a number of random moves, and save unique states."""
    for i in range(attempts):
        states = []
        board = Board(size)

        for j in range(num_of_moves):
            board._make_random_move()

            if board.state not in states:
                states.append(board.state)


if __name__ == "__main__":
    generate_board_states(1, 5)
