
from contextlib import redirect_stdout

path = 'text.txt'
with open(path, 'w') as fobj:
    with redirect_stdout(fobj):
        help(redirect_stdout)

'''
we are redirecting stdout to a file. 
When we call Python’s help, instead of printing to stdout,
it gets saved directly to the file. 
You could also redirect stdout to some kind of buffer or a 
text control type widget from a user interface toolkit like Tkinter or wxPython.
'''

##if you wanted to redirect stdout, you would do something like this:
import sys

path = 'text.txt'

with open(path, 'w') as fobj:
    sys.stdout = fobj
    help(sum)
