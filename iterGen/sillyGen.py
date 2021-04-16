# Demo of a generator...

def silly_generator():
    yield "Python"
    yield "Rocks"
    yield "So do you!"
gen = silly_generator()
print (next(gen))
#'Python'

print (next(gen))
#'Rocks'

print (next(gen))
#'So do you!'

print (next(gen))
#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 15, in <module>
# print (next(gen))
#StopIteration:

gen = silly_generator()
for item in gen:
    print(item)

#Python
#Rocks
#So do you!
