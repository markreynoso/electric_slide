"""Test for the priority_q module."""

import pytest


def test_construct_a_new_start_node():
    """Test that a starting node can be constructed."""
    from electric_slide.scripts.priority_q import Node
    n = Node([[1, 2, 3], [4, 5, 6], [7, 8, 9]], None, None)
    assert n.move is None
    assert n.prev is None
    assert n.state == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_construct_a_new_child_node_after_start(n0):
    """Test that creating a child Node points to parent."""
    from electric_slide.scripts.priority_q import Node
    next_state = [[1, 2, 3], [4, 5, 6], [7, 9, 8]]
    n = Node(next_state, (2, 3), n0)
    assert n.move == (2, 3)
    assert n.prev is n0
    assert n.state == next_state


def test_construct_a_new_child_node(n1):
    """Test that creating a child Node points to parent."""
    from electric_slide.scripts.priority_q import Node
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
    from electric_slide.scripts.priority_q import Node
    node1 = Node([[1, 2, 3], [4, 5, 6], [9, 7, 8]], (1, 2), None)
    node2 = Node([[1, 2, 3], [4, 5, 6], [9, 7, 8]], (3, 1), n1)
    assert node1 is not node2
    assert node1 == node2


def test_inequality_between_nodes_with_different_states():
    """Test that Nodes with different states are inequivalent."""
    from electric_slide.scripts.priority_q import Node
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


def test_constructing_a_priority_q_is_empty():
    """Test that a new PriorityQ is empty."""
    from electric_slide.scripts.priority_q import PriorityQ
    q = PriorityQ()
    assert q.values == {}


def test_pushing_new_prioity_value_adds_to_queue(empty_queue):
    """Test that a pushing a new priority into a queue adds the value."""
    q = empty_queue
    q.push('a', 1)
    assert q.values == {1: ['a']}


def test_pushing_value_same_priority_adds_to_queue(empty_queue):
    """Test that a pushing a new value to the same priority adds the value."""
    q = empty_queue
    q.push('a', 1)
    q.push('b', 1)
    assert q.values == {1: ['a', 'b']}


def test_pushing_different_priorities_adds_to_queue(empty_queue):
    """Test that a pushing a diff priorities adds both values."""
    q = empty_queue
    q.push('a', 1)
    q.push('b', 2)
    assert q.values == {1: ['a'], 2: ['b']}


def test_pushing_different_many_values_to_priorities_adds_to_queue(empty_queue):
    """Test that a pushing values to diff priorities adds all values."""
    q = empty_queue
    q.push('a', 1)
    q.push('b', 2)
    q.push('c', 1)
    assert q.values == {1: ['a', 'c'], 2: ['b']}


def test_popping_from_empty_queue_raises_error(empty_queue):
    """Test that popping from empty queue raises ValueError."""
    with pytest.raises(ValueError):
        empty_queue.pop()


def test_popping_only_item_from_queue_empties_it(empty_queue):
    """Test that poppingonly item from queue empties it."""
    empty_queue.push('a', 2)
    empty_queue.pop()
    assert empty_queue.values == {}


def test_popping_value_returns_lowest_priority(filled_queue):
    """Test that popping values from queue removes lowest priority."""
    assert filled_queue.pop() == 'e'


def test_popping_only_value_from_priority_removes_priority(filled_queue):
    """Test that popping only value from priority removes priority."""
    filled_queue.pop()
    assert 0 not in filled_queue.values


def test_popping_value_from_queue_does_not_remove_priority(filled_queue):
    """Test that popping value from multi value priority."""
    filled_queue.pop()
    assert filled_queue.pop() == 'd'
    assert 1 in filled_queue.values


def test_found_priority_of_value_in_queue_is_correct(filled_queue):
    """Test that the priority found is correct."""
    assert filled_queue.priority('c') == 4


def test_found_priority_of_value_not_in_queue_is_none(filled_queue):
    """Test that the priority found of value not in queue is None."""
    assert filled_queue.priority('x') is None


def test_removing_value_without_priority_removes_from_queue(filled_queue):
    """Test that removing from the queue without giving a priority works."""
    filled_queue.remove('d')
    assert filled_queue.priority('d') is None


def test_removing_only_value_with_priority_removes_priority(filled_queue):
    """Test that removing only value from priority remove priority."""
    filled_queue.remove('f', 6)
    assert filled_queue.priority('f') is None
    assert 6 not in filled_queue.values


def test_removing_value_with_priority_removes_from_queue(filled_queue):
    """Test that removing from the queue with a priority works."""
    filled_queue.remove('d', 1)
    assert filled_queue.priority('d') is None


def test_removing_value_not_in_queue_gets_error(filled_queue):
    """Test that removing item not in queue raises a KeyError."""
    with pytest.raises(KeyError):
        filled_queue.remove('x')


def test_removing_value_with_incorrect_priority_gets_error(filled_queue):
    """Test that removing item with incorrect priority raises ValueError."""
    with pytest.raises(ValueError):
        filled_queue.remove('d', 6)


def test_removing_value_with_priority_not_in_queue_gets_error(filled_queue):
    """Test that removing item with invalid priority raises KeyError."""
    with pytest.raises(KeyError):
        filled_queue.remove('d', 9)
