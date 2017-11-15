"""Tests for the a-star algorithm and heuristic functions."""

import pytest


@pytest.fixture
def scrambled_board_complexity_6():
    """Return a scrambled board of complexity 6."""
    return [[1, 2, 3], [4, 9, 8], [7, 6, 5]]


@pytest.fixture
def scrambled_board_complexity_2():
    """Return a scrambled board of complexity 2."""
    return [[1, 2, 9], [4, 5, 3], [7, 8, 6]]


def test_manhattan_distance_returns_an_int(scrambled_board_complexity_6):
    """Test manhattan distance returns an instance of an int."""
    from electric_slide.scripts.algorithm import manhattan_distance
    assert isinstance(manhattan_distance(scrambled_board_complexity_6), int)


def test_manhattan_distance_returns_correct_heuristic_value(scrambled_board_complexity_6):
    """Test that heuristic value returned is correct."""
    from electric_slide.scripts.algorithm import manhattan_distance
    assert manhattan_distance(scrambled_board_complexity_6) == 6


def test_manhattan_distance_correctly_returns_0_for_solved_board():
    """Test that the heuristic value for a solved board is zero."""
    from electric_slide.scripts.algorithm import manhattan_distance
    solved_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert manhattan_distance(solved_board) == 0


def test_astar_correctly_terminates(scrambled_board_complexity_6):
    """Test that astar will correctly solve a scrambled board state."""
    from electric_slide.scripts.algorithm import a_star
    assert a_star(scrambled_board_complexity_6)


def test_astar_correctly_returns_path_of_moves(scrambled_board_complexity_6):
    """Test that astar returns a list of board states to the solution."""
    from electric_slide.scripts.algorithm import a_star
    assert isinstance(a_star(scrambled_board_complexity_6), list)


def test_astar_returns_list_with_solved_state_as_final_entry(scrambled_board_complexity_6):
    """Test that the solved board states list correctly contains final solved state."""
    from electric_slide.scripts.algorithm import a_star
    solved_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert solved_board in a_star(scrambled_board_complexity_6)


def test_astar_returns_single_entry_list_for_solved_state():
    """Test that when passed a solved state, a_star returns that state."""
    from electric_slide.scripts.algorithm import a_star
    solved_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]] == a_star(solved_board)


def test_astar_correctly_solves_complexity_2(scrambled_board_complexity_2):
    """Test that astar solves correctly for low heuristic values."""
    from electric_slide.scripts.algorithm import a_star
    assert len(a_star(scrambled_board_complexity_2)) == 3


def test_astar_correcty_solves_complexity_17():
    """Test that astar solves correctly for high heuristic values."""
    from electric_slide.scripts.algorithm import a_star
    assert a_star([[5, 1, 3], [8, 2, 4], [7, 9, 6]])


def test_astar_correcty_solves_complexity_25():
    """Test that astar solves correctly for high heuristic values."""
    from electric_slide.scripts.algorithm import a_star
    assert a_star([[6, 1, 5], [7, 2, 9], [3, 8, 4]])


def test_greedy_pure_correcty_solves_complexity_25():
    """Test that greedy pure solves correctly for high heuristic values."""
    from electric_slide.scripts.algorithm import greedy_pure_search
    assert greedy_pure_search([[6, 1, 5], [7, 2, 9], [3, 8, 4]])


# The test below is for the most complex board state, which it passes, but takes a long time
# def test_astar_correcty_solves_complexity_31():
#     """Test that astar solves correctly for high heuristic values."""
#     from electric_slide.scripts.algorithm import a_star
#     assert a_star([[8, 6, 7], [2, 5, 4], [3, 9, 1]])
