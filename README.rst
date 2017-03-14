Simple Q Service
================

A simple q'ing service written with Flask-API

::

    $ PYTHONPATH="$PYTHONPATH:." python -m sqs
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!

Then::

    $ curl http://127.0.0.1:5000
    {"q": "q"}

This is a browseable API, so you may point a browser to the URL as well.