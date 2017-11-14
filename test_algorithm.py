"""Tests for the a-star algorithm and heuristic functions."""

from copy import deepcopy

import pytest


@pytest.fixture
def sol_board():
    """Create a solved board."""
    from board import Board
    return Board()


