# get_rt22.py
#
# From the notes.  Access the CTA website and fetch information
# about route 22 buses.  Write to a file 'rt22.xml'.

# For Python 3, change import urllib to urllib.request

import urllib
u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()
f = open('rt22.xml', 'wb') # writes in binary. 
'''
On Unix systems (Linux, Mac OS X, etc.), binary mode does nothing - they treat text files the same way that any other files are treated. On Windows, however, text files are written with slightly modified line endings. This causes a serious problem when dealing with actual binary files, like exe or jpg files. Therefore, when opening files which are not supposed to be text, even in Unix, you should use wb or rb. Use plain w or r only for text files.
'''
f.write(data)
f.close()
print('Wrote rt22.xml')
