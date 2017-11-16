"""."""
from pyramid import testing
from pyramid.testing import DummyRequest

import pytest


@pytest.fixture
def dummy_request():
    """Instantiate a fake HTTP Request, complete with a database session."""
    return testing.DummyRequest()


def test_shuffle_route(dummy_request):
    """Test if shuffle route returns dictionary."""
    from electric_slide.views.default import shuffle
    state = shuffle(dummy_request)
    assert isinstance(state, dict)


def test_shuffle_route_returns_dict_with_key_shuffle(dummy_request):
    """Test if shuffle route returns dictionary."""
    from electric_slide.views.default import shuffle
    state = shuffle(dummy_request)
    assert state['shuffle']


def test_shuffle_route_returns_list_of_lists(dummy_request):
    """Test if shuffle route returns list."""
    from electric_slide.views.default import shuffle
    state = shuffle(dummy_request)
    assert isinstance(state['shuffle'][0], list)


def test_shuffle_route_returns_list_length_of_3(dummy_request):
    """Test if shuffle route returns list of length 3."""
    from electric_slide.views.default import shuffle
    state = shuffle(dummy_request)
    assert len(state['shuffle']) == 3


def test_shuffle_route_returns_list_of_3_each_len_3(dummy_request):
    """Test if shuffle route returns list of lists length 3."""
    from electric_slide.views.default import shuffle
    state = shuffle(dummy_request)
    assert len(state['shuffle'][0]) == 3
    assert len(state['shuffle'][1]) == 3
    assert len(state['shuffle'][2]) == 3


def test_solve_tree_returns_dict(dummy_request):
    """Test solve tree returns dictionary."""
    from electric_slide.views.default import solve_tree
    dummy_request.params = {'state': [[4, 3, 5], [2, 9, 1], [7, 8, 6]]}
    state_list = solve_tree(dummy_request)
    assert isinstance(state_list, dict)


def test_solve_tree_returns_dict_with_key_solution(dummy_request):
    """Test solve tree returns dict with key solution."""
    from electric_slide.views.default import solve_tree
    dummy_request.params = {'state': [[4, 3, 5], [2, 9, 1], [7, 8, 6]]}
    state_list = solve_tree(dummy_request)
    assert state_list['solution']


def test_solve_tree_returns_list_of_lists_len_3(dummy_request):
    """Test solve tree returns list of lists length 3."""
    from electric_slide.views.default import solve_tree
    dummy_request.params = {'state': [[4, 3, 5], [2, 9, 1], [7, 8, 6]]}
    state_list = solve_tree(dummy_request)
    for state in state_list['solution']:
        assert len(state) == 3


def test_solve_astar_returns_dict(dummy_request):
    """Test solve astar returns dictionary."""
    from electric_slide.views.default import solve_astar
    dummy_request.params = {'state': [[4, 3, 5], [2, 9, 1], [7, 8, 6]]}
    state_list = solve_astar(dummy_request)
    assert isinstance(state_list, dict)


def test_solve_astar_returns_dict_with_key_solution(dummy_request):
    """Test solve astar returns dict with key solution."""
    from electric_slide.views.default import solve_astar
    dummy_request.params = {'state': [[4, 3, 5], [2, 9, 1], [7, 8, 6]]}
    state_list = solve_astar(dummy_request)
    assert state_list['solution']


def test_solve_astar_returns_list_of_lists_len_3(dummy_request):
    """Test solve astar returns list of lists length 3."""
    from electric_slide.views.default import solve_astar
    dummy_request.params = {'state': [[4, 3, 5], [2, 9, 1], [7, 8, 6]]}
    state_list = solve_astar(dummy_request)
    for state in state_list['solution']:
        assert len(state) == 3


def test_solve_greedy_returns_dict(dummy_request):
    """Test solve astar returns dictionary."""
    from electric_slide.views.default import solve_greedy
    dummy_request.params = {'state': [[4, 3, 5], [2, 9, 1], [7, 8, 6]]}
    state_list = solve_greedy(dummy_request)
    assert isinstance(state_list, dict)


def test_solve_greedy_returns_dict_with_key_solution(dummy_request):
    """Test solve astar returns dict with key solution."""
    from electric_slide.views.default import solve_greedy
    dummy_request.params = {'state': [[4, 3, 5], [2, 9, 1], [7, 8, 6]]}
    state_list = solve_greedy(dummy_request)
    assert state_list['solution']


def test_solve_astar_returns_list_of_lists_len_3(dummy_request):
    """Test solve astar returns list of lists length 3."""
    from electric_slide.views.default import solve_astar
    dummy_request.params = {'state': [[4, 3, 5], [2, 9, 1], [7, 8, 6]]}
    state_list = solve_astar(dummy_request)
    for state in state_list['solution']:
        assert len(state) == 3
