
import pickle

with open('entry.pickle', 'rb') as f:
     entry = pickle.load(f)

b = pickle.dumps(entry)             #① dumps for inMem, dump for file
print (type(b))                     #②
#<class 'bytes'>

entry3 = pickle.loads(b)            #③ loads for inMem, load for file.
print (entry3 == entry)             #④
#True

print (entry3 is entry)
#False
