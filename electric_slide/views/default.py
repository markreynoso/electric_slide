"""."""

# from pyramid.response import Response
from pyramid.view import view_config
from electric_slide.scripts.board import Board
import json


@view_config(route_name='home', renderer='electric_slide:/templates/index.jinja2')
def home_view(request):
    """."""
    return {}


@view_config(route_name='data', renderer='electric_slide:/templates/data.jinja2')
def data_view(request):
    """."""
    return {}


@view_config(route_name='about', renderer='electric_slide:/templates/about.jinja2')
def about_view(request):
    """."""
    return {}


@view_config(route_name='tree', renderer='json')
def solve_tree(request):
    """Solve the current board using the Tree method."""
    with open("electric_slide/data/state_almanac_data.json") as f:
        state_almanac = json.load(f)
    b = Board()
    b.solve(request.params["state"], state_almanac)

    return {"solution": b.previous_states}


@view_config(route_name='shuffle', renderer='json')
def shuffle(request):
    """Generate a random state for the front end."""
    from random import choice
    with open("electric_slide/data/state_almanac_data.json") as f:
        state_almanac = json.load(f)

    return {"shuffle": json.loads(choice(list(state_almanac)))}
