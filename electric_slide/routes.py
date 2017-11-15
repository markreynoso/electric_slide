"""."""


def includeme(config):
    """Some routes."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('data', '/data')
    config.add_route('about', '/about')
    config.add_route('tree', '/api/solve/tree')
    config.add_route('shuffle', '/api/shuffle')
