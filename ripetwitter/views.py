from pyramid.renderers import get_renderer
from pyramid.httpexceptions import HTTPFound
from twitter import *
from pyramid.view import view_config
import simplejson as json

token = ''
token_secret = ''
consumer_key = ''
consumer_secret = ''

@view_config(route_name='home', renderer='templates/index.pt')


def index_view(request):
    tweets = []
    title = ''
    view_type = ''
    t = Twitter(
            auth=OAuth(
                token=token,
                token_secret=token_secret,
                consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                )
           )
    if t:
        title = request.GET.get('title', '')
        search_term = request.GET.get('search_term', None)
        view_type = request.GET.get('view_type', 'single')
        tweet_number = request.GET.get('tweet_number', 6)
        if search_term:
            searches =  t.search.tweets(q=search_type+search_term)
            if searches:
                if 'statuses' in searches:
                    tweets = searches['statuses'][:int(tweet_number)]
    return {'tweets': tweets, 
            'title': title,
            'type': view_type}
