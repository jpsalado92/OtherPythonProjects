#next is http://www.pythonchallenge.com/pc/def/oxygen.html


import os
from urllib.request import urlopen
import re

"""

for filename in os.listdir("Challenge_6"):
    print(filename)
    f_path="Challenge_6\\"+filename
    f = open(f_path, "r")
    print(f.read())

"""


end = False

from zipfile import is_zipfile
from zipfile import ZipFile

zip_path = "Challenge_6\\channel.zip"
f_path = "Challenge_6\\" + "90052.txt"
commentslist = []
zf = ZipFile(zip_path)
while not end:
    try:
        f = open(f_path, "r")
        f_str = f.read()
        print('f_str: {}'.format(f_str))
        match = re.search(r'is [\w.-][0123456789]+', f_str)
        print('Match: {}'.format(str(match)))
        result = match.group()[3:]
        print(result)
        f_path = "Challenge_6\\" + result + ".txt"
        print('')
        commentslist.append(zf.getinfo(result + ".txt").comment.decode("utf-8"))
    except:
        end = True

print(commentslist)
print("".join(commentslist))

"""

from zipfile import is_zipfile
from zipfile import ZipFile

commentslist = []
zip_path = "Challenge_6\\channel.zip"
zf = ZipFile(zip_path)
for filename in os.listdir("Challenge_6"):
    try:
        #print(filename)
        f_path = "Challenge_6\\" + filename
        commentslist.append(zf.getinfo(filename).comment.decode("utf-8"))

    except:
        pass

commentslist="".join(commentslist)
print(commentslist)
"""
