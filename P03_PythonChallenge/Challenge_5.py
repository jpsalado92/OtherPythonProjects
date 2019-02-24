#next is http://www.pythonchallenge.com/pc/def/channel.html


import re
import pickle
print(pickle.HIGHEST_PROTOCOL)
from urllib.request import urlopen

# url = "http://www.pythonchallenge.com/pc/def/banner.p"
# page = urlopen(url)
# content = str(page.read())[2:-1].encode()
# print(content)
# file = open("Challenge_5", "wb")

# file.write(content)
# file.close()

file = open("Challenge_5_banner.p", "rb")
data = pickle.load(file)
print(data)

for list in data:
    print("".join([k * v for k, v in list]))

