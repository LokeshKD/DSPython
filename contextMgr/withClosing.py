'''
from contextlib import contextmanager

@contextmanager
def closing(db):
    try:
        yield db.conn()
    finally:
        db.close()

Basically what we’re doing is creating a closing function that’s wrapped in a contextmanager. 
This is the equivalent of what the closing class does.
The difference is that instead of a decorator, we can use the closing class itself in our with statement.
'''

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.google.com')) as webpage:
    for line in webpage:
        # process the line
        pass

'''
we open a url page but wrap it with our closing class. 
This will cause the handle to the web page to be closed 
once we fall out of the with statement’s code block.
'''
