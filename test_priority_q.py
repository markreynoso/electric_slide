"""Test for the priority_q module."""

import pytest


START_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


@pytest.fixture
def n0():
    """A starting Node."""
    from priority_q import Node
    return Node(START_STATE, None, None)


@pytest.fixture
def n1(n0):
    """A child Node after n0."""
    from priority_q import Node
    next_state = [[1, 2, 3], [4, 5, 6], [7, 9, 8]]
    return Node(next_state, (2, 3), n0)


@pytest.fixture
def chain7(n0, n1):
    """A chain of 5 nodes."""
    from priority_q import Node
    n2 = Node([[1, 2, 3], [4, 5, 6], [9, 7, 8]], (1, 3), n1)
    n3 = Node([[1, 2, 3], [9, 5, 6], [4, 7, 8]], (1, 2), n2)
    n4 = Node([[9, 2, 3], [1, 5, 6], [4, 7, 8]], (1, 1), n3)
    n5 = Node([[2, 9, 3], [1, 5, 6], [4, 7, 8]], (2, 1), n4)
    return Node([[2, 5, 3], [1, 9, 6], [4, 7, 8]], (2, 2), n5)


def test_construct_a_new_start_node():
    """Test that a starting node can be constructed."""
    from priority_q import Node
    n = Node(START_STATE, None, None)
    assert n.move is None
    assert n.prev is None
    assert n.state == START_STATE


def test_construct_a_new_child_node_after_start(n0):
    """Test that creating a child Node points to parent."""
    from priority_q import Node
    next_state = [[1, 2, 3], [4, 5, 6], [7, 9, 8]]
    n = Node(next_state, (2, 3), n0)
    assert n.move == (2, 3)
    assert n.prev is n0
    assert n.state == next_state


def test_construct_a_new_child_node(n1):
    """Test that creating a child Node points to parent."""
    from priority_q import Node
    next_state = [[1, 2, 3], [4, 5, 6], [9, 7, 8]]
    n = Node(next_state, (1, 3), n1)
    assert n.move == (1, 3)
    assert n.prev is n1
    assert n.state == next_state


def test_path_from_single_node_is_one_long(n0):
    """Test that the path from a starting Node is one long."""
    assert len(n0.path()) == 1


def test_path_from_single_node_is_its_state(n0):
    """Test that the path from a starting Node is its own state."""
    assert n0.path()[0] == n0.state


def test_path_from_second_node_is_two_long(n1):
    """Test that the path from the second Node is two long."""
    assert len(n1.path()) == 2


def test_path_from_second_node_is_its_state_and_parent_state(n0, n1):
    """Test that the path from the second Node is its own state then the parent state."""
    assert n1.path()[0] == n1.state
    assert n1.path()[1] == n0.state


def test_path_from_end_of_chain_is_appropriate_length(chain7):
    """Test that the path from end of a longer chain is long enough."""
    assert len(chain7.path()) == 7


def test_path_has_all_states_in_the_chain(chain7):
    """Test that all the states are in the path from the end of the chain."""
    path = chain7.path()
    curr = chain7
    for state in path:
        assert state == curr.state
        curr = curr.prev


def test_equality_between_nodes_with_the_same_state(n1):
    """Test that Nodes with the same state are equivalent."""
    from priority_q import Node
    node1 = Node([[1, 2, 3], [4, 5, 6], [9, 7, 8]], (1, 2), None)
    node2 = Node([[1, 2, 3], [4, 5, 6], [9, 7, 8]], (3, 1), n1)
    assert node1 is not node2
    assert node1 == node2


def test_inequality_between_nodes_with_different_states():
    """Test that Nodes with different states are inequivalent."""
    from priority_q import Node
    node1 = Node([[1, 2, 3], [4, 5, 6], [9, 7, 8]], (1, 2), None)
    node2 = Node([[9, 2, 3], [1, 5, 6], [4, 7, 8]], (1, 2), None)
    assert node1 is not node2
    assert node1 != node2


def test_find_all_legal_moves_for_open_corner(n0):
    """Test that all legal moves are found for an open corner."""
    assert sorted(n0.legal_moves()) == sorted([(3, 2), (2, 3)])


def test_find_all_legal_moves_for_open_side(n1):
    """Test that all legal moves are found for an open side."""
    assert sorted(n1.legal_moves()) == sorted([(1, 3), (3, 3), (2, 2)])


def test_find_all_legal_moves_for_open_center(chain7):
    """Test that all legal moves are found for an open center."""
    assert sorted(chain7.legal_moves()) == sorted([(1, 2), (2, 1), (3, 2), (2, 3)])
