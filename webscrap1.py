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

# sample url: http://py4e-data.dr-chuck.net/known_by_Fikret.html
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = int(input('Enter count: '))
position = int(input('Enter position: '))

#reduce position by 1 since index starts from 0
position -= 1
urllist = list()


for x in range(count):
    # Retrieve all of the anchor tags for the current tag and find the one at the position needed
    tags = soup('a')
    tag = tags[position]
    email = tag.get('href', None)
    urllist.append(email)

    # use current email as a start
    url = str(email)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

for i in urllist:
    print('Retrieving: ', i)

