
import pickle


entry = {}                                                                                         #②
entry['title'] = 'Dive into history, 2009 edition'
entry['article_link'] = 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'
entry['comments_link'] = None
entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
entry['tags'] = ('diveintopython', 'docbook', 'html')
entry['published'] = True

import time
entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009')                                #③
print (entry['published_date'])
print("Writing to pickle file")

with open('entry.pickle', 'wb') as f:    #②
    pickle.dump(entry, f) 


# Read the pickle file and print in human readable form.
print("Readin from pickle file")
with open('entry.pickle', 'rb') as f:            #③
     entry = pickle.load(f)                      #④
 
print (entry)
