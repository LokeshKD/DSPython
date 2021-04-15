from contextlib import suppress

with suppress(FileNotFoundError):
    with open('fauxfile.txt') as fobj:
        for line in fobj:
            print(line)

'''
Here we import suppress and pass it the exception that we want to ignore, 
which in this case is the FileNotFoundError exception.
If we run this code, we will note that nothing happens as the file does 
not exist, but an error is also not raised. 
It should be noted that this context manager is reentrant.
'''
