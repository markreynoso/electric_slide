"""."""

from pyramid.response import Response
from pyramid.view import view_config
from electric_slide.scripts.board import Board
import json


@view_config(route_name='home', renderer='electric_slide:/templates/index.jinja2')
def home_view(request):
    """View for the home page."""
    return {'title': 'home'}


@view_config(route_name='nick', renderer='electric_slide:/templates/nick.jinja2')
def home_view(request):
    """View for the secret nick page."""
    return {'title': 'nick'}


@view_config(route_name='data', renderer='electric_slide:/templates/data.jinja2')
def data_view(request):
    """View for the data page."""
    return {'title': 'data'}


@view_config(route_name='about', renderer='electric_slide:/templates/about.jinja2')
def about_view(request):
    """View for the about page."""
    return {'title': 'about'}


@view_config(route_name='states-data', renderer='json')
def states_data_json(request):
    """Send the count of the number of states in each complexity."""
    with open('electric_slide/data/state_almanac_data.json') as f:
        all_states = json.load(f)
    all_val = list(all_states.values())
    return {c: all_val.count(c) for c in range(max(all_val) + 1)}


@view_config(route_name='solving-data', renderer='json')
def solving_data_json(request):
    """Send all the historical data of each algorithm solving all complexities."""
    with open('electric_slide/data/tree_data.json') as f:
        tree_data = json.load(f)
    with open('electric_slide/data/a_star_data.json') as f:
        a_star_data = json.load(f)
    with open('electric_slide/data/greedy_data.json') as f:
        greedy_data = json.load(f)
    solving_data = {}
    for complexity in tree_data:
        solving_data[complexity] = {
            'tree': {
                'time': tree_data[complexity]['time'],
                'moves': tree_data[complexity]['moves']
            },
            'a_star': {
                'time': a_star_data[complexity]['time'],
                'moves': a_star_data[complexity]['moves']
            },
            'greedy': {
                'time': greedy_data[complexity]['time'],
                'moves': greedy_data[complexity]['moves']
            }
        }
    return solving_data


@view_config(route_name='tree', renderer='json')
def solve_tree(request):
    """Solve the current board using the Tree method."""
    with open("electric_slide/data/state_almanac_data.json") as f:
        state_almanac = json.load(f)
    b = Board()
    b.solve(json.loads(request.params["state"]), state_almanac)

    return {"solution": b.previous_states}


@view_config(route_name='astar', renderer='json')
def solve_astar(request):
    """Solve the current board using the A* method."""
    from electric_slide.scripts.algorithm import a_star
    state = json.loads(request.params["state"])
    return {"solution": a_star(state)}


@view_config(route_name='greedy', renderer='json')
def solve_greedy(request):
    """Solve the current board using the Greedy method."""
    from electric_slide.scripts.algorithm import greedy_pure_search
    state = json.loads(request.params["state"])
    return {"solution": greedy_pure_search(state)}


@view_config(route_name='shuffle', renderer='json')
def shuffle(request):
    """Generate a random state for the front end."""
    from random import choice
    with open("electric_slide/data/state_almanac_data.json") as f:
        state_almanac = json.load(f)

    return {"shuffle": json.loads(choice(list(state_almanac)))}
