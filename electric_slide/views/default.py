# from pyramid.response import Response
from pyramid.view import view_config




@view_config(route_name='home', renderer='electric_slide:/templates/index.jinja2')
def home_view(request):
    return {}


@view_config(route_name='data', renderer='electric_slide:/templates/data.jinja2')
def data_view(request):
    return {}


@view_config(route_name='about', renderer='electric_slide:/templates/about.jinja2')
def about_view(request):
    return {}


@view_config(route_name='states-data', renderer='json')
def states_data_json(request):
    import json
    with open('electric_slide/data/state_almanac_data.json') as f:
        all_states = json.load(f)
    all_val = list(all_states.values())
    return {c: all_val.count(c) for c in range(max(all_val) + 1)}
