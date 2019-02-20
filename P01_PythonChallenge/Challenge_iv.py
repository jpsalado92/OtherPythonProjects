import re

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022"
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=82682"
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579"


i = 0
while i < 400:
    src = urlopen(url)
    html_str = str(src.read())
    #print( html_str)
    match = re.search(r'is [\w.-][123456789]+', html_str)
    result = match.group()[3:]
    print(result)
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + result
    #print(url)

    # If-statement after search() tests if it succeeded
    if match:
        print('Iteration: {} found'.format(i))
    else:
        print
        print('did not find')
    i += 1
