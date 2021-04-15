from contextlib import ExitStack
with ExitStack() as stack:
    file_objects = [stack.enter_context(open(filename))
        for filename in filenames]


'''
This code basically creates a series of context managers inside the list comprehension. 
The ExitStack maintains a stack of registered callbacks that it will call in reverse 
order when the instance it closed, which happens when we exit the the bottom of the with statement
'''
