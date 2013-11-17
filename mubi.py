# coding: utf-8

import requests
from lxml.html import fromstring


class MubiException(Exception):
    pass


class Mubi(object):
    def __init__(self, email, password):
        if not email or not password:
            raise ValueError(
                "Credentials must be specified. "
                "Pass them into Mubi constructor"
            )

        self.session = requests.Session()
        self.me = self._login(email, password)

    def _login(self, email, password):
        login_html = self.session.get('https://mubi.com/login').content
        auth_token = (fromstring(login_html)
                      .xpath("//input[@name='authenticity_token']/@value"))
        payload = {
            'utf8': '✓',
            'authenticity_token': auth_token,
            'email': email,
            'password': password,
            'x': 0,
            'y': 0
        }

        response = self.session.post('https://mubi.com/session', data=payload)

        # Once a user successfully authenticates, MUBI will redirect a user
        # to the homepage, otherwise the login page will be shown.
        if response.url == 'http://mubi.com/home':
            # Yet another redirect to the user profile page, e.g. /users/12345
            user_url = self.session.get('http://mubi.com/profile').url
            user_id = user_url.split('/')[-1]
            return user_id
        elif response.url == 'https://mubi.com/login':
            raise MubiException("Sorry, email or password doesn't work")
