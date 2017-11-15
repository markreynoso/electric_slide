"""Tests for the board module."""

# from copy import deepcopy

import pytest

from random import choice

import json

from electric_slide.scripts.board import PracticeBoard


@pytest.fixture
def sol_board():
    """Create a solved board."""
    from electric_slide.scripts.board import Board
    return Board()


ALL_COORDS = []
for y in range(1, 4):
    for x in range(1, 4):
        ALL_COORDS.append((x, y))


def test_empty_constructor_makes_board_in_solved_state():
    """Test that the Board constructor creates a solved board."""
    from electric_slide.scripts.board import Board
    b = Board()
    assert b.state == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_constructed_board_has_correct_open_cell(sol_board):
    """Test that the new Board has open cell in bottom corner."""
    assert sol_board.open_cell_coords == (3, 3)


def test_constructed_board_has_correct_legal_moves(sol_board):
    """Test that the new Board has legal moves around the empty cell."""
    assert sorted(sol_board.legal_moves) == sorted([(3, 2), (2, 3)])


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
    from electric_slide.scripts.board import Board
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


def test_slide_swaps_tiles_horizontally_then_vertically(sol_board):
    """Test that slide moves tiles correctly horiz then vert."""
    sol_board.slide((2, 3))
    sol_board.slide((2, 2))
    assert sol_board.state == [[1, 2, 3], [4, 9, 6], [7, 5, 8]]


def test_slide_swaps_tiles_vertically_then_horizontally(sol_board):
    """Test that slide moves tiles correctly horiz then vert."""
    sol_board.slide((3, 2))
    sol_board.slide((2, 2))
    assert sol_board.state == [[1, 2, 3], [4, 9, 5], [7, 8, 6]]


def test_make_random_move_results_in_new_state(sol_board):
    """Test that make random move does not return current state."""
    sol_board._make_random_move()
    assert sol_board.state != [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_make_random_move_changes_state(sol_board):
    """Test make random move changes board to a new state."""
    state = str(sol_board.state)
    for i in range(20):
        sol_board._make_random_move()
        assert str(sol_board.state) != state
        state = str(sol_board.state)


def test_make_random_move_does_not_return_to_previous_state(sol_board):
    """Test make random move does not return a previous board state."""
    previous = str(sol_board.previous_states)
    for i in range(20):
        sol_board._make_random_move()
        assert str(sol_board.state) not in previous
        previous = str(sol_board.previous_states)


def test_determine_legal_moves_correct_number_of_moves(sol_board):
    """Test _determine_legal_moves generates the correct number of moves."""
    sol_board.state = [[2, 5, 3], [1, 9, 6], [4, 7, 8]]
    sol_board._determine_legal_moves((2, 2))
    assert len(sol_board.legal_moves) == 4
    sol_board.state = [[1, 2, 3], [7, 6, 9], [5, 4, 8]]
    sol_board._determine_legal_moves((3, 2))
    assert len(sol_board.legal_moves) == 3
    sol_board.state = [[1, 2, 9], [5, 6, 3], [4, 7, 8]]
    sol_board._determine_legal_moves((3, 1))
    assert len(sol_board.legal_moves) == 2


def test_solve_returns_something(sol_board):
    """Test that the solve method doesn't return None."""
    assert sol_board.solve([[1, 2, 9], [5, 6, 3], [4, 7, 8]])

with open("electric_slide/data/state_almanac_data.json") as f:
        state_almanac = json.load(f)

RANDOM_STATES = [json.loads(choice(list(state_almanac))) for i in range(20)]


def test_solve_end_state_is_solved(sol_board):
    """Test that the state of the board after running solve is correct."""
    sol_board.solve(choice(RANDOM_STATES))
    assert sol_board.state == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_solve_end_open_cell_coords(sol_board):
    """Test that the open cell of the board after running solve is correct."""
    sol_board.solve(choice(RANDOM_STATES))
    assert sol_board.open_cell_coords == (3, 3)


@pytest.mark.parametrize('state', RANDOM_STATES)
def test_solve_solves_board_ideally(sol_board, state):
    """Test that the solve method solves in an ideal number of moves."""
    random_starting_state = state
    ideal_num_of_moves = state_almanac[str(state)]
    assert sol_board.solve(random_starting_state) == ideal_num_of_moves


def test_empty_constructor_makes_pboard_error():
    """Test that the PracticeBoard constructor needs a state param."""
    with pytest.raises(TypeError):
        PracticeBoard()


def test_constructed_pboard_has_correct_open_cell():
    """Test that the new pboard has the correct open cell."""
    pb = PracticeBoard([[1, 2, 9], [5, 6, 3], [4, 7, 8]])
    assert pb.practice_open_cell_coords == (3, 1)


def test_constructed_pboard_has_correct_size():
    """Test that the new pboard has the correct size."""
    pb = PracticeBoard([[1, 2, 9], [5, 6, 3], [4, 7, 8]])
    assert pb.practice_size == 3


def test_pboard_determine_legal_moves_finds_all_moves():
    """Test that the legal moves are correctly determined in a pboard."""
    pb = PracticeBoard([[2, 5, 3], [1, 9, 6], [4, 7, 8]])
    assert sorted(pb.determine_legal_moves()) == sorted([(2, 1), (2, 3), (1, 2), (3, 2)])
    pb = PracticeBoard([[1, 2, 3], [7, 6, 9], [5, 4, 8]])
    assert sorted(pb.determine_legal_moves()) == sorted([(3, 3), (3, 1), (2, 2)])
    pb = PracticeBoard([[1, 2, 9], [5, 6, 3], [4, 7, 8]])
    assert sorted(pb.determine_legal_moves()) == sorted([(2, 1), (3, 2)])


def test_practice_slide_returns_correctthing():
    """Test that the practice_slide method returns correctthing."""
    pb = PracticeBoard([[1, 2, 9], [5, 6, 3], [4, 7, 8]])
    assert pb.practice_slide((2, 1)) == [[1, 9, 2], [5, 6, 3], [4, 7, 8]]
    pb = PracticeBoard([[2, 5, 3], [1, 9, 6], [4, 7, 8]])
    assert pb.practice_slide((2, 3)) == [[2, 5, 3], [1, 7, 6], [4, 9, 8]]
    pb = PracticeBoard([[1, 2, 3], [7, 6, 9], [5, 4, 8]])
    assert pb.practice_slide((3, 3)) == [[1, 2, 3], [7, 6, 8], [5, 4, 9]]
