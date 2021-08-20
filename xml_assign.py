#import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter url: ')
if len(address) < 1:
  address = 'http://py4e-data.dr-chuck.net/comments_42.xml'

uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)

# Get comments/comment/count
results = tree.findall('.//count')
sum = 0

for x in results:
  sum += int(x.text)

print('Counts: ', len(results))
print('Sum: ', sum)
