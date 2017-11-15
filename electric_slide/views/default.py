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