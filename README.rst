mubi |Build Status|
===================

A good starting point for getting some data from `mubi.com`_. Since MUBI
doesn't provide a public API, you need to do all the things manually.
``mubi.py`` is created to help you with the login process.

Powered by awesome `Requests`_.

Usage
-----

To access the most interesting part of the `mubi.com`_ content you'll
need to be logged in. It's time for ``mubi.py``:

.. code:: python

    >>> from mubi import login, mubicom
    >>> session, me = login('email', 'password', identify=True)

    # Show your user id
    >>> print(me)
    '123456'

    # Use the requests.Session object (now with cookies) as usual
    >>> session.get(mubicom('/films'))
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

Install
-------

::

    $ pip install mubi

.. _mubi.com: http://mubi.com
.. _Requests: http://www.python-requests.org/en/latest/
.. _examples.py: https://github.com/mstolyarchuk/mubi.py/blob/master/examples.py

.. |Build Status| image:: https://travis-ci.org/mstolyarchuk/mubi.py.png
