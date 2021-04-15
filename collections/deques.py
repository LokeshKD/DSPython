'''
According to the Python documentation, deques “are a generalization of stacks and queues”. 
They are pronounced “deck” which is short for "double-ended queue".
They are a replacement container for the Python list. 
Deques are thread-safe and support memory efficient appends and pops from either side of the deque.
'''

from collections import deque
import string



d = deque(string.ascii_lowercase)
for letter in d:
    print(letter)

d.append('bork')
print (d)
#deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
#       'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'bork'])

d.appendleft('test')
print (d)
#deque(['test', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'bork'])

d.rotate(1)
print (d)
#deque(['bork', 'test', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#       'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])


#
# This code works in much the same way as Linux’s tail program does.
#
def get_last(filename, n=5):
    """
    Returns the last n lines from the file
    """
    try:
        with open(filename) as f:
            return deque(f, n)
    except OSError:
        print("Error opening file: {}".format(filename))
        raise

