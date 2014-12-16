README
======

Prerequisites
-------------

* Python 2.6
* Twitter development OAuth account: https://dev.twitter.com/oauth
* Make

Background
----------

This buildout creates a Python-based Pyramid web application. It runs off port 6543 as a default Pyramid application taken from https://github.com/svx/pyramid-buildout
In production, the application can run off a specificed port set within the production.ini file.

No database is required for this application.

The Twitter Python package is used to connect the Pyramid application to the Twitter API. More information can be found at: https://pypi.python.org/pypi/twitter

Setup
--------

Git clone [Git repo]

Navigate to the ripe.meetingtwitter directory:

	cd ripe.meetingtwitter

Then run the buildout using the provided Make file. If you don't have Make installed, you can run bin/buildout manually.

For a development (reload) application:

	make devel

For a production application using supervisord:

	make production
    	bin/supervisord

The development environment is used to test the Twitterwall.

This should build the Pyramid application.

Adding Your Oauth ID
-------------------

Add your Twitter Oauth information in the views.py file:

token = ''
token_secret = ''
consumer_key = ''
consumer_secret = ''

Starting Up the Instance
------------------------

In development mode:

	make dev-reload

In production, supervisord is installed. Thefore you can use that to start up the instances:
 
	bin/supervisorctl
    	start pyramids

If you don't want to use supervisord, you can run the bin/pserve [development.ini/production.ini] &

Application Parameters
------------------------------

search_term = hashtag to search for. The hash symbol isn't required.

title = title you want to be shown on the Twitter wall.

view_type = full, show six tweets. By default one tweet is displayed.

tweet_number = number of tweets (default is six). The view_type parameter is also required.

Example
--------
Six tweets:
	http://localhost:6543/?search_term=RIPE&title=RIPE TWITTERWALL&view_type=full
Five tweets:
	http://localhost:6543/?search_term=RIPE&title=RIPE TWITTERWALL&view_type=full&tweet_number=5
One tweet:
	http://localhost:6543/?search_term=RIPE&title=RIPE TWITTERWALL

Usage
-----

You can toggle the browser's zoom functionality to make the tweets bigger or smaller.

Please remember Twitters API usage policy: https://dev.twitter.com/rest/public/rate-limiting

Cleaning up the Buildout
------------------------

If you have a problem with the buildout, or want to run it again, run: 

	make clean

Then run the required buildout command.

License
------------------------

This library is distributed under the BSD License. See: https://raw.github.com/RIPE-NCC/rpki-commons/master/LICENSE.txt
