"""

ripe-twitter project - 2014

"""

from pyramid.config import Configurator


def route_base(config):
    config.add_route('home', '/')


def route_static(config):
    """ route marker """
    config.add_static_view('static', 'ripetwitter:static/',
                           cache_max_age=3600)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include(route_base)
    config.include(route_static)
    config.scan()
    return config.make_wsgi_app()
