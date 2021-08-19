# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# sample url
# http://py4e-data.dr-chuck.net/comments_1338410.html
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

counts = list()
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
    number = int(tag.contents[0])
    counts.append(number)
print('counts', len(counts))
print('sum', sum(counts))