"""Various tests for comparator.py."""

from electric_slide.scripts.algorithm import greedy_pure_search, a_star
from electric_slide.scripts.board import Board
from electric_slide.scripts.comparator import record_solution_stats
import json
import pytest

with open("electric_slide/data/state_almanac_data.json") as f:
        state_almanac = json.load(f)


ONE_OF_EACH = [("[[1, 2, 3], [4, 5, 6], [7, 9, 8]]", 1), ("[[1, 2, 9], [4, 5, 3], [7, 8, 6]]", 2), ("[[1, 2, 3], [4, 8, 5], [7, 9, 6]]", 3), ("[[9, 2, 3], [1, 4, 5], [7, 8, 6]]", 4), ("[[1, 5, 2], [9, 4, 3], [7, 8, 6]]", 5), ("[[1, 2, 3], [5, 6, 8], [4, 7, 9]]", 6), ("[[1, 2, 3], [7, 4, 9], [5, 8, 6]]", 7), ("[[1, 3, 9], [7, 2, 6], [5, 4, 8]]", 8), ("[[1, 9, 5], [4, 3, 6], [7, 2, 8]]", 9), ("[[1, 6, 2], [5, 7, 3], [4, 8, 9]]", 10), ("[[1, 6, 2], [4, 8, 9], [7, 3, 5]]", 11), ("[[7, 3, 9], [2, 1, 5], [8, 4, 6]]", 12), ("[[2, 3, 4], [1, 7, 9], [8, 6, 5]]", 13), ("[[1, 2, 3], [6, 7, 4], [9, 5, 8]]", 14), ("[[7, 5, 3], [9, 1, 6], [2, 4, 8]]", 15), ("[[7, 4, 1], [3, 9, 2], [5, 6, 8]]", 16), ("[[1, 6, 2], [5, 4, 3], [8, 9, 7]]", 17), ("[[2, 5, 9], [4, 1, 6], [7, 3, 8]]", 18), ("[[2, 6, 8], [7, 3, 5], [4, 9, 1]]", 19), ("[[3, 4, 1], [5, 7, 6], [9, 2, 8]]", 20)]


@pytest.mark.parametrize('state, comp', ONE_OF_EACH)
def test_record_output_types_tree(state, comp):
    """Test that the output types of record_solution_stats for tree are correct."""
    b = Board()
    state = json.loads(state)
    time, moves = record_solution_stats('test_data.json', b.solve, state, comp, state_almanac)
    assert type(time) == float
    assert type(moves) == int


@pytest.mark.parametrize('state, comp', ONE_OF_EACH)
def test_record_output_types_a_star(state, comp):
    """Test that the output types of record_solution_stats for a_star are correct."""
    state = json.loads(state)
    time, moves = record_solution_stats('test_data.json', a_star, state, comp)
    assert type(time) == float
    assert type(moves) == int


@pytest.mark.parametrize('state, comp', ONE_OF_EACH)
def test_record_output_types_greedy(state, comp):
    """Test that the output types of record_solution_stats for greedy are correct."""
    state = json.loads(state)
    time, moves = record_solution_stats('test_data.json', greedy_pure_search, state, comp)
    assert type(time) == float
    assert type(moves) == int

with open('electric_slide/data/test_data.json', 'w') as file:
            json.dump({}, file)
