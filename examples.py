"""
This file contains the next steps with mubi.py.

Before start to pulling data from mubi.com with your requests,
look at the Jeff Atwood's helpful recommendations about web scraping:
http://meta.stackoverflow.com/a/446

We use lxml library for parsing needs. Why?
http://docs.python-guide.org/en/latest/scenarios/scrape
"""

import requests
from lxml.html import fromstring
from mubi import login, mubicom


mubi, me = login(identify=True)

def simple_example():
    """You are awesome."""
    url = mubicom('/home')
    doc = fromstring(mubi.get(url).text)
    username = doc.xpath("//div[@class='username']/h1/text()")
    print(username)


def get_film_title(id_or_slug):
    """MUBI creates a 301 permanent redirect to the page with url
    contains film slug if you initially use id as identifier.

    Examples:
    >>> get_film_title('456')
    'Mouchette'

    >>> get_film_title('mouchette')
    'Mouchette'
    """
    url = mubicom('/films/' + id_or_slug)
    doc = fromstring(mubi.get(url).text)
    return doc.xpath("//h1[contains(@class, 'film_title')]/text()")[0]

# Below are few examples of retrieving JSON data using MUBI internal services.

def watchlist_json():
    """Retrivies the latest film you would like to see."""
    url = mubicom('/users/{}/watchlist.json'.format(me))
    watchlist = mubi.get(url).json()
    print(watchlist[0])

def tooltip_json(film_id):
    """Retrives a tooltip data for the specific film.

    You may find tooltips on the http://mubi.com/watch page.
    Open the page, then hover over a film.

    Response from the server contains the following keys: cast, directors,
    duration, excerpt, id, primary_country, title and year.

    >>> tooltip_json('456')
    u'Mouchette, by Robert Bresson'
    """
    url = mubicom('/services/films/tooltip')

    payload = {'id': film_id, 'country_code': 'US', 'locale': 'en-US'}
    tooltip = mubi.get(url, params=payload).json()
    directors = tooltip['directors'].values()

    return u'{0}, by {1}'.format(tooltip['title'], ', '.join(directors))

def ratings_json(film_ids=None, page=None):
    """Retrives your ratings for the specific films.
    MUBI paginates ratings by 20 items per page.
    """
    # If parameters aren't specified you'll get the 20 latest ratings.
    payload = None

    if film_ids:
        payload = [('films_id[]', id) for id in film_ids]
    elif page:
        payload = {'page': page}

    url = mubicom('/users/{}/ratings.json', params=payload)
    ratings = mubi.get(url).json()
    return ratings
