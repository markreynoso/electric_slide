"""Test fixtures for decision tree and A* solve methods."""
import pytest


@pytest.fixture
def solved_board():
    """Instantiate a solved board."""
    from electric_slide.scripts.board import Board
    return Board()


@pytest.fixture
def n0():
    """A starting Node."""
    from electric_slide.scripts.priority_q import Node
    return Node([[1, 2, 3], [4, 5, 6], [7, 8, 9]], None, None)


@pytest.fixture
def n1(n0):
    """A child Node after n0."""
    from electric_slide.scripts.priority_q import Node
    next_state = [[1, 2, 3], [4, 5, 6], [7, 9, 8]]
    return Node(next_state, (2, 3), n0)


@pytest.fixture
def chain7(n0, n1):
    """A chain of 5 nodes."""
    from electric_slide.scripts.priority_q import Node
    n2 = Node([[1, 2, 3], [4, 5, 6], [9, 7, 8]], (1, 3), n1)
    n3 = Node([[1, 2, 3], [9, 5, 6], [4, 7, 8]], (1, 2), n2)
    n4 = Node([[9, 2, 3], [1, 5, 6], [4, 7, 8]], (1, 1), n3)
    n5 = Node([[2, 9, 3], [1, 5, 6], [4, 7, 8]], (2, 1), n4)
    return Node([[2, 5, 3], [1, 9, 6], [4, 7, 8]], (2, 2), n5)


@pytest.fixture
def empty_queue():
    """An empty PriorityQ."""
    from electric_slide.scripts.priority_q import PriorityQ
    return PriorityQ()


@pytest.fixture
def filled_queue():
    """A filled PriorityQ."""
    from electric_slide.scripts.priority_q import PriorityQ
    q = PriorityQ()
    q.push('a', 1)
    q.push('b', 2)
    q.push('c', 4)
    q.push('d', 1)
    q.push('e', 0)
    q.push('f', 6)
    q.push('g', 4)
    return q
