# coding: utf-8

import os
import re
import requests


class MubiException(Exception):
    pass


def mubicom(path, use_ssl=False):
    """Returns a full url for the given path."""
    protocol = 'https' if use_ssl else 'http'
    return '{0}://mubi.com/{1}'.format(protocol, path.lstrip('/'))

def login(email=None, password=None, session=None, identify=False):
    """Returns a logged in requests.Session object using your credentials.

    You can either pass their directly or specify via environment variables.
    Enable identify parameter to get a tuple in the form (session object, user id).
    If given email address or password fails you get a MubiException.
    """
    email = email or os.getenv('MUBI_EMAIL')
    password = password or os.getenv('MUBI_PASSWORD')
    if not email or not password:
        raise ValueError("Credentials must be specified. "
                         "You can either pass their directly into login method "
                         "or specify via environment variables.")

    if session is None:
        session = requests.Session()

    login_html = session.get(mubicom('login', True)).text

    # Everybody stand back!
    m = re.search('<input\s+name="authenticity_token".*?value="(.*?)"\s*\/>',
                  login_html)
    if m is None:
        raise ValueError("Unable to match authenticity token. "
                         "It seems the login page has changed.")

    response = session.post(mubicom('session', True), data={
        'utf8': '✓',
        'authenticity_token': m.group(0),
        'email': email,
        'password': password,
        'x': 0,
        'y': 0
    })
    # Once a user successfully authenticates, MUBI will redirect a user
    # to the homepage, otherwise the login page will be shown.
    if response.url == mubicom('home'):
        if identify:
            # Yet another redirect to the user profile page, e.g. /users/123456
            user_url = session.get(mubicom('profile')).url
            user_id = user_url.split('/')[-1]
            return session, user_id
        return session
    elif response.url == mubicom('login', True):
        raise MubiException("Sorry, email or password doesn't work")
