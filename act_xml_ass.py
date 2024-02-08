##actual assignment on xml data extraction

#08/02/2024 07:35am

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET

#bypassing ssl certificates

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#taking input from the user

sumlist = list()

userinput = input('Enter your url:')

#opening user xml urllink

userxml = urllib.request.urlopen(userinput, context=ctx)
dataxml = userxml.read()
dataxml.decode()
tree = ET.fromstring(dataxml)

treelist = tree.findall('comments/comment')

print('Item Count:', len(treelist))

for comment in treelist:
    val = int(comment.find('count').text)
    sumlist.append(val)

print('Item Sum:', sum(sumlist))
