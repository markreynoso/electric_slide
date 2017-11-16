"""Various tests for comparator.py."""

from electric_slide.scripts.algorithm import greedy_pure_search, a_star
from electric_slide.scripts.board import Board
from electric_slide.scripts.comparator import record_solution_stats


def test_record_output_types():
    """Test that the output types of record_solution_stats are correct."""
