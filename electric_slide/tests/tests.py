"""."""
from pyramid.testing import DummyRequest

import pytest


@pytest.fixture
def dummy_request():
    """Instantiate a fake HTTP Request, complete with a database session."""
    return DummyRequest()


def test_home_view_returns_dict(dummy_request):
    """Test that the home_view route returns a dict."""
    from electric_slide.views.default import home_view
    assert isinstance(home_view(dummy_request), dict)


def test_data_view_returns_dict(dummy_request):
    """Test that the data_view route returns a dict."""
    from electric_slide.views.default import data_view
    assert isinstance(data_view(dummy_request), dict)


def test_about_view_returns_dict(dummy_request):
    """Test that the about_view route returns a dict."""
    from electric_slide.views.default import about_view
    assert isinstance(about_view(dummy_request), dict)


def test_states_data_json_returns_dict(dummy_request):
    """Test that the states_data_json route returns a dict."""
    from electric_slide.views.default import states_data_json
    assert isinstance(states_data_json(dummy_request), dict)


def test_solving_data_json_returns_dict(dummy_request):
    """Test that the solving_data_json route returns a dict."""
    from electric_slide.views.default import solving_data_json
    assert isinstance(solving_data_json(dummy_request), dict)


def test_solving_data_json_dict_is_len_32(dummy_request):
    """Test that the solving_data_json route returns a dict of len 32."""
    from electric_slide.views.default import solving_data_json
    assert len(solving_data_json(dummy_request)) == 32


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
    dummy_request.params = {'state': "[[4, 3, 5], [2, 9, 1], [7, 8, 6]]"}
    state_list = solve_tree(dummy_request)
    assert isinstance(state_list, dict)


def test_solve_tree_returns_dict_with_key_solution(dummy_request):
    """Test solve tree returns dict with key solution."""
    from electric_slide.views.default import solve_tree
    dummy_request.params = {'state': "[[4, 3, 5], [2, 9, 1], [7, 8, 6]]"}
    state_list = solve_tree(dummy_request)
    assert state_list['solution']


def test_solve_tree_returns_list_of_lists_len_3(dummy_request):
    """Test solve tree returns list of lists length 3."""
    from electric_slide.views.default import solve_tree
    dummy_request.params = {'state': "[[4, 3, 5], [2, 9, 1], [7, 8, 6]]"}
    state_list = solve_tree(dummy_request)
    for state in state_list['solution']:
        assert len(state) == 3


def test_solve_astar_returns_dict(dummy_request):
    """Test solve astar returns dictionary."""
    from electric_slide.views.default import solve_astar
    dummy_request.params = {'state': "[[4, 3, 5], [2, 9, 1], [7, 8, 6]]"}
    state_list = solve_astar(dummy_request)
    assert isinstance(state_list, dict)


def test_solve_astar_returns_dict_with_key_solution(dummy_request):
    """Test solve astar returns dict with key solution."""
    from electric_slide.views.default import solve_astar
    dummy_request.params = {'state': "[[4, 3, 5], [2, 9, 1], [7, 8, 6]]"}
    state_list = solve_astar(dummy_request)
    assert state_list['solution']


def test_solve_astar_returns_list_of_lists_len_3(dummy_request):
    """Test solve astar returns list of lists length 3."""
    from electric_slide.views.default import solve_astar
    dummy_request.params = {'state': "[[4, 3, 5], [2, 9, 1], [7, 8, 6]]"}
    state_list = solve_astar(dummy_request)
    for state in state_list['solution']:
        assert len(state) == 3


def test_solve_greedy_returns_dict(dummy_request):
    """Test solve astar returns dictionary."""
    from electric_slide.views.default import solve_greedy
    dummy_request.params = {'state': "[[4, 3, 5], [2, 9, 1], [7, 8, 6]]"}
    state_list = solve_greedy(dummy_request)
    assert isinstance(state_list, dict)


def test_solve_greedy_returns_dict_with_key_solution(dummy_request):
    """Test solve astar returns dict with key solution."""
    from electric_slide.views.default import solve_greedy
    dummy_request.params = {'state': "[[4, 3, 5], [2, 9, 1], [7, 8, 6]]"}
    state_list = solve_greedy(dummy_request)
    assert state_list['solution']


# def test_solve_astar_returns_list_of_lists_len_3(dummy_request):
#     """Test solve astar returns list of lists length 3."""
#     from electric_slide.views.default import solve_astar
#     dummy_request.params = {'state': "[[4, 3, 5], [2, 9, 1], [7, 8, 6]]"}
#     state_list = solve_astar(dummy_request)
#     for state in state_list['solution']:
#         assert len(state) == 3
