"""Test fixtures for decision tree and A* solve methods."""
import pytest


@pytest.fixture
def solved_board():
    """Instantiate a solved board."""
    from board import Board
    return Board()
