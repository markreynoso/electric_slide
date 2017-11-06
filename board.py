"""Define the Board and Cell classes."""

from random import randint


class Cell(object):
    """Make an instance of the Cell class."""

    def __init__(self, num, coords):
        """Constructor for the Cell class."""
        self.tile = num
        self.coords = coords

    def __repr__(self):
        """Show the tile value rather than the object."""
        return str(self.tile)


class PracticeBoard(object):
    """Make an instance of the PracticeBoard class."""

    def __init__(self, state, open_cell_coords, size):
        """Constructor for the PracticeBoard class."""
        self.state = state
        self.open_cell_coords = open_cell_coords
        self.size = size

    def _tile_number_at_coords(self, coords):
        """Take in 1-indexed x-y coordinates and return the tile number at that location."""
        return self.state[coords[1] - 1][coords[0] - 1].tile

    def _cell_at_coords(self, coords):
        """Take in 1-indexed x-y coordinates and return the Cell object at that location."""
        return self.state[coords[1] - 1][coords[0] - 1]

    def slide(self, coords):
        """Slide the tile at the given coordinates into the open cell."""
        tile_to_move = self._tile_number_at_coords(coords)
        self._cell_at_coords(coords).tile = self.size ** 2
        self._cell_at_coords(self.open_cell_coords).tile = tile_to_move
        self.open_cell_coords = coords

        return self.state


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
        y_coord = 1
        for i in range(size):
            x_coord = 1
            row = []
            for j in range(size):
                row.append(Cell(num, (x_coord, y_coord)))
                num += 1
                x_coord += 1
            y_coord += 1
            self.state.append(row)

    def _tile_number_at_coords(self, coords):
        """Take in 1-indexed x-y coordinates and return the tile number at that location."""
        return self.state[coords[1] - 1][coords[0] - 1].tile

    def _cell_at_coords(self, coords):
        """Take in 1-indexed x-y coordinates and return the Cell object at that location."""
        return self.state[coords[1] - 1][coords[0] - 1]

    def slide(self, coords):
        """Slide the tile at the given coordinates into the open cell."""
        self.previous_states.append(self.state)
        tile_to_move = self._tile_number_at_coords(coords)
        self._cell_at_coords(coords).tile = self.size ** 2
        self._cell_at_coords(self.open_cell_coords).tile = tile_to_move
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
        check_board = PracticeBoard(self.state, self.open_cell_coords, self.size)

        potential_move = self.legal_moves[randint(0, len(self.legal_moves) - 1)]

        if check_board.slide(potential_move) in self.previous_states:
            self.legal_moves.remove(potential_move)
            self._make_random_move()

        else:
            self.slide(potential_move)


def generate_board_states(num_of_moves, attempts, size=3):
    """From a solved board, make a given number of random moves, and save unique board states."""
    states = []

    for i in range(attempts):
        board = Board(size)

        for j in range(num_of_moves):
            board._make_random_move()

        if board.state not in states:
            states.append(board.state)

    for state in states:
        print(state)


if __name__ == "__main__":
    generate_board_states(1, 10)
