# mubi

A good starting point for getting some data from [mubi.com](http://mubi.com). Since MUBI doesn't provide a public API, you need to do all the things manually.
`mubi.py` is a simple wrapper around awesome [Requests](http://www.python-requests.org) session object and created to help you with the login process.

Use `pip install mubi.py` to get it.

## Usage


To access the most interesting part of the mubi.com content you'll need to login using your MUBI email address and password:
```python
from mubi import Mubi
m = Mubi('email', 'password')
```

Once you successfully logged in two public attributes will become available for you: `me` variable and `request` method:
```python
>>> m.me # your user id
'123456'

>>> m.request('GET', '/festivals')
<Response [200]>
```

What's next you ask? Do requests and separate the wheat from the chaff!
