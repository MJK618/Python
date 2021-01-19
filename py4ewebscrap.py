#Py4e
#Course 3 week 4
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input('Enter - ')
count = int(input("Enter count :"))
pos = int(input("Enter position : "))
for i in range(count):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    tag = tags[pos-1]
    url = str(tag.get('href', None))
    print(tag.get('href', None))
