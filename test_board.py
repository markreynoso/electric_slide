"""Tests for the board module."""

import pytest


@pytest.fixture
def sol_board():
    """Create a solved board."""
    from board import Board
    return Board()


ALL_COORDS = []
for y in range(1, 4):
    for x in range(1, 4):
        ALL_COORDS.append((x, y))


def test_empty_constructor_makes_board_in_solved_state():
    """Test that the Board constructor creates a solved board."""
    from board import Board
    b = Board()
    assert b.state == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_constructed_board_has_correct_open_cell(sol_board):
    """Test that the new Board has open cell in bottom corner."""
    assert sol_board.open_cell_coords == (3, 3)


def test_constructed_board_has_correct_legal_moves(sol_board):
    """Test that the new Board has legal moves around the empty cell."""
    assert sorted(sol_board.legal_moves) == sorted([(3, 2), (2, 3)])


@pytest.mark.parametrize('coords, result', [(ALL_COORDS[n], n + 1) for n in range(9)])
def test_tile_at_coords_gets_correct_number(coords, result):
    """Test that the tile found at the given coords is correct."""
    from board import Board
    b = Board()
    assert b._tile_at_coords(coords) == result


LEGAL_MOVES = [
    ((1, 1), [(1, 2), (2, 1)]),
    ((1, 2), [(1, 1), (1, 3), (2, 2)]),
    ((1, 3), [(1, 2), (2, 3)]),
    ((2, 1), [(1, 1), (3, 1), (2, 2)]),
    ((2, 2), [(1, 2), (2, 1), (3, 2), (2, 3)]),
    ((2, 3), [(1, 3), (3, 3), (2, 2)]),
    ((3, 1), [(2, 1), (3, 2)]),
    ((3, 2), [(3, 1), (3, 3), (2, 2)]),
    ((3, 3), [(3, 2), (2, 3)]),
]


@pytest.mark.parametrize('coords, result', LEGAL_MOVES)
def test_determine_legal_moves_finds_all_moves(coords, result):
    """Test that the legal moves are correctly determined around any coords."""
    from board import Board
    b = Board()
    b._determine_legal_moves(coords)
    assert sorted(b.legal_moves) == sorted(result)


def test_slide_swaps_tiles_vertically(sol_board):
    """Test that slide moves tiles correctly vertically."""
    sol_board.slide((3, 2))
    assert sol_board.state == [[1, 2, 3], [4, 5, 9], [7, 8, 6]]


def test_slide_swaps_tiles_vertically_multiple_times(sol_board):
    """Test that slide moves tiles correctly vertically."""
    sol_board.slide((3, 2))
    sol_board.slide((3, 1))
    assert sol_board.state == [[1, 2, 9], [4, 5, 3], [7, 8, 6]]


def test_slide_swaps_tiles_vertically_reverse(sol_board):
    """Test that slide moves tiles correctly vertically."""
    sol_board.slide((3, 2))
    sol_board.slide((3, 3))
    assert sol_board.state == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_slide_swaps_tiles_horizontally(sol_board):
    """Test that slide moves tiles correctly horizontally."""
    sol_board.slide((2, 3))
    assert sol_board.state == [[1, 2, 3], [4, 5, 6], [7, 9, 8]]


def test_slide_swaps_tiles_horizontally_multiple_times(sol_board):
    """Test that slide moves tiles correctly horizontally."""
    sol_board.slide((2, 3))
    sol_board.slide((1, 3))
    assert sol_board.state == [[1, 2, 3], [4, 5, 6], [9, 7, 8]]


def test_slide_swaps_tiles_horizontally_reverse(sol_board):
    """Test that slide moves tiles correctly horizontally."""
    sol_board.slide((2, 3))
    sol_board.slide((3, 3))
    assert sol_board.state == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
