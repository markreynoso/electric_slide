"""Initialize electric slide app."""
from pyramid.config import Configurator


def main(global_config, **settings):
    """Return a Pyramid WSGI application."""
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.routes')
    config.add_static_view(name='static', path='electric_slide:static')
    config.scan()
    return config.make_wsgi_app()
