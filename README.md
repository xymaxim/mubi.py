# mubi

A good starting point for getting some data from [mubi.com](http://mubi.com). Since MUBI doesn't provide a public API, you need to do all the things manually.
`mubi.py` created to help you with the login process.

Powered by awesome [Requests](http://www.python-requests.org/en/latest/).

## Usage

First, type `pip install mubi` to get it.

Then, to access the most interesting part of the mubi.com content you'll need to be logged in. It's time for `mubi.py`:

```python
>>> from mubi import login, mubicom
>>> session, me = login('email', 'password', identify=True)

# Show your user id
>>> print(me)
'123456'

# Use the requests.Session object (now with cookies) as usual
>>> session.get(mubicom('/watch'))
<Response [200]>
```

What's next you ask? Do requests!

For real life usage and useful tips, please see [examples.py](https://github.com/mstolyarchuk/mubi.py/examples.py).
