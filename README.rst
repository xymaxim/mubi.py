mubi |Build Status|
===================

A good starting point for getting some data from `mubi.com`_. Since MUBI
doesn't provide a public API, you need to do all the things manually.
``mubi.py`` is created to help you with the login process.

Powered by awesome `Requests`_.

Getting started
---------------

Usage
~~~~~

To access the most interesting part of the `mubi.com`_ content you'll
need to be logged in. It's time for ``mubi.py``:

.. code:: python

    >>> from mubi import login, mubicom
    >>> session, me = login('email', 'password', identify=True)

    # Show your user id
    >>> print(me)
    '123456'

    # Use the requests.Session object (now with cookies) as usual
    >>> session.get(mubicom('/films/showing'))
    <Response [200]>

To be a good internet citizen provide some information about yourself:

.. code:: python

    >>> import requests
    >>> from mubi import login

    >>> s = requests.Session()
    >>> s.headers.update({
    ...     # Add something useful
    ...     'User-Agent': 'Mr. Robot/1.0 (http://github.com/example/repo beep@example.com)'
    >>> })

    >>> mubi = login('email', 'password', session=s)
    
Politeness policy
~~~~~~~~~~~~~~~~~

In order to be polite towards MUBI and their website (and not to get blocked), try to follow this:

- Respect the robots.txt file
- Identify yourself in the User-Agent header
- Use gzip compression. *Requests* |automatically_decompresses|_ *gzip-encoded responses*
- Put a delay between each requests
- Use the right formats. *Yes, there is no API but you could use a JSON content instead of scraping HTML*
- Read the Terms of Service and Privacy Policy

Install
-------

Install the package via pip:

.. code:: sh

    $ pip install mubi

.. _mubi.com: http://mubi.com
.. _Requests: http://www.python-requests.org/en/latest/
.. _examples.py: https://github.com/mstolyarchuk/mubi.py/blob/master/examples.py
.. _robots.txt: http://www.robotstxt.org/orig.html

.. |automatically_decompresses| replace:: *automatically decompresses*
.. _automatically_decompresses: http://www.python-requests.org/en/latest/community/faq/#encoded-data

.. |Build Status| image:: https://travis-ci.org/mstolyarchuk/mubi.py.png
                 :target: https://travis-ci.org/mstolyarchuk/mubi.py
