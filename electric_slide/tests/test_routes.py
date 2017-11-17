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


@pytest.fixture(scope="session")
def testapp(request):
    """Functional test for app."""
    from webtest import TestApp
    from electric_slide import main

    return TestApp(main({}))


def test_home_route_gets_200_status_code(testapp):
    """Test that the home route gets 200 status code."""
    response = testapp.get("/")
    assert response.status_code == 200


def test_home_route_has_three_sliding_puzzles(testapp):
    """Test that the home route has three sliding puzzles."""
    response = testapp.get("/")
    assert len(response.html.find_all('div', 'puzzle-container')) == 3


def test_data_route_gets_200_status_code(testapp):
    """Test that the data route gets 200 status code."""
    response = testapp.get("/data")
    assert response.status_code == 200


def test_data_route_has_three_charts(testapp):
    """Test that the data route has three charts."""
    response = testapp.get("/data")
    assert len(response.html.find_all('canvas')) == 3


def test_about_route_gets_200_status_code(testapp):
    """Test that the about route gets 200 status code."""
    response = testapp.get("/about")
    assert response.status_code == 200


def test_about_route_has_four_profile_cards(testapp):
    """Test that the about route has four profile cards."""
    response = testapp.get("/about")
    assert len(response.html.find_all('div', 'card')) == 4


def test_nick_route_gets_200_status_code(testapp):
    """Test that the nick route gets 200 status code."""
    response = testapp.get("/nick")
    assert response.status_code == 200


def test_nick_route_has_three_sliding_puzzles(testapp):
    """Test that the nick route has three sliding puzzles of nick."""
    response = testapp.get("/nick")
    assert len(response.html.find_all('div', 'puzzle-container')) == 3
    assert 'nick' in str(response.html.find('div', 'tile').find('img'))


def test_invalid_route_goes_to_404_page(testapp):
    """Test that the invalid route goes to 404 page."""
    response = testapp.get("/fun", status=404)
    assert '404' in str(response.html.find('h1'))


def test_states_data_route_gets_200_status_code(testapp):
    """Test that the states data route gets 200 status code."""
    response = testapp.get("/api/data/states")
    assert response.status_code == 200


def test_states_data_route_responds_with_json(testapp):
    """Test that the states data route returns a JSON file."""
    import json
    response = testapp.get("/api/data/states")
    assert json.loads(response.text) == response.json


def test_states_data_route_has_quantities_for_all_complexities(testapp):
    """Test that the states data route has ints for all complexities."""
    response = testapp.get("/api/data/states")
    assert len(response.json) == 32
    assert isinstance(response.json['0'], int)


def test_solving_data_route_gets_200_status_code(testapp):
    """Test that the solving data route gets 200 status code."""
    response = testapp.get("/api/data/solve")
    assert response.status_code == 200


def test_solving_data_route_responds_with_json(testapp):
    """Test that the solving data route returns a JSON file."""
    import json
    response = testapp.get("/api/data/solve")
    assert json.loads(response.text) == response.json


def test_solving_data_route_has_all_algorithms_at_each_complexity(testapp):
    """Test that the solving data route has all algorithms at each complexity."""
    response = testapp.get("/api/data/solve")
    assert len(response.json) == 32
    assert 'tree' in response.json['0']
    assert 'greedy' in response.json['0']
    assert 'a_star' in response.json['0']


def test_solving_data_route_has_data_for_tree_algorithm(testapp):
    """Test that the solving data route has data for the tree."""
    response = testapp.get("/api/data/solve")
    assert 'time' in response.json['0']['tree']
    assert 'moves' in response.json['0']['tree']


def test_solving_data_route_tree_algorithm_data_is_list(testapp):
    """Test that the solving data route has tree data as a list."""
    response = testapp.get("/api/data/solve")
    assert isinstance(response.json['0']['tree']['time'], list)
    assert isinstance(response.json['0']['tree']['moves'], list)


def test_solving_data_route_has_data_for_greedy_algorithm(testapp):
    """Test that the solving data route has data for the greedy."""
    response = testapp.get("/api/data/solve")
    assert 'time' in response.json['0']['greedy']
    assert 'moves' in response.json['0']['greedy']


def test_solving_data_route_greedy_algorithm_data_is_list(testapp):
    """Test that the solving data route has greedy data as a list."""
    response = testapp.get("/api/data/solve")
    assert isinstance(response.json['0']['greedy']['time'], list)
    assert isinstance(response.json['0']['greedy']['moves'], list)


def test_solving_data_route_has_data_for_astar_algorithm(testapp):
    """Test that the solving data route has data for the astar."""
    response = testapp.get("/api/data/solve")
    assert 'time' in response.json['0']['a_star']
    assert 'moves' in response.json['0']['a_star']


def test_solving_data_route_astar_algorithm_data_is_list(testapp):
    """Test that the solving data route has astar data as a list."""
    response = testapp.get("/api/data/solve")
    assert isinstance(response.json['0']['a_star']['time'], list)
    assert isinstance(response.json['0']['a_star']['moves'], list)


def test_shuffle_route_gets_200_status_code(testapp):
    """Test that the shuffle route gets 200 status code."""
    response = testapp.get("/api/shuffle")
    assert response.status_code == 200


def test_shuffle_route_responds_with_json(testapp):
    """Test that the shuffle route returns a JSON file."""
    import json
    response = testapp.get("/api/shuffle")
    assert json.loads(response.text) == response.json


def test_shuffle_route_sends_a_single_random_board(testapp):
    """Test that the shuffle route sends a single random board."""
    response = testapp.get("/api/shuffle")
    assert len(response.json['shuffle']) == 3
    assert len(response.json['shuffle'][0]) == 3
    assert len(response.json['shuffle'][1]) == 3
    assert len(response.json['shuffle'][2]) == 3


def test_tree_solve_route_gets_200_status_code(testapp):
    """Test that the tree solving route gets 200 status code."""
    response = testapp.get("/api/solve/tree?state=[[1,2,3],[4,5,6],[9,7,8]]")
    assert response.status_code == 200


def test_tree_solve_route_responds_with_json(testapp):
    """Test that the tree solving route returns a JSON file."""
    import json
    response = testapp.get("/api/solve/tree?state=[[1,2,3],[4,5,6],[9,7,8]]")
    assert json.loads(response.text) == response.json


def test_tree_solve_route_returns_solution(testapp):
    """Test that the tree solving route returns the solution from the tree."""
    response = testapp.get("/api/solve/tree?state=[[1,2,3],[4,5,6],[9,7,8]]")
    assert response.json['solution'] == [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                                         [[1, 2, 3], [4, 5, 6], [7, 9, 8]],
                                         [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]


def test_greedy_solve_route_gets_200_status_code(testapp):
    """Test that the greedy solving route gets 200 status code."""
    response = testapp.get("/api/solve/greedy?state=[[1,2,3],[4,5,6],[9,7,8]]")
    assert response.status_code == 200


def test_greedy_solve_route_responds_with_json(testapp):
    """Test that the greedy solving route returns a JSON file."""
    import json
    response = testapp.get("/api/solve/greedy?state=[[1,2,3],[4,5,6],[9,7,8]]")
    assert json.loads(response.text) == response.json


def test_greedy_solve_route_returns_solution(testapp):
    """Test that the greedy solving route returns the solution from the greedy."""
    response = testapp.get("/api/solve/greedy?state=[[1,2,3],[4,5,6],[9,7,8]]")
    assert response.json['solution'] == [[[1, 2, 3], [4, 5, 6], [9, 7, 8]],
                                         [[1, 2, 3], [4, 5, 6], [7, 9, 8]],
                                         [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]


def test_astar_solve_route_gets_200_status_code(testapp):
    """Test that the astar solving route gets 200 status code."""
    response = testapp.get("/api/solve/astar?state=[[1,2,3],[4,5,6],[9,7,8]]")
    assert response.status_code == 200


def test_astar_solve_route_responds_with_json(testapp):
    """Test that the astar solving route returns a JSON file."""
    import json
    response = testapp.get("/api/solve/astar?state=[[1,2,3],[4,5,6],[9,7,8]]")
    assert json.loads(response.text) == response.json


def test_astar_solve_route_returns_solution(testapp):
    """Test that the astar solving route returns the solution from the astar."""
    response = testapp.get("/api/solve/astar?state=[[1,2,3],[4,5,6],[9,7,8]]")
    assert response.json['solution'] == [[[1, 2, 3], [4, 5, 6], [9, 7, 8]],
                                         [[1, 2, 3], [4, 5, 6], [7, 9, 8]],
                                         [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
