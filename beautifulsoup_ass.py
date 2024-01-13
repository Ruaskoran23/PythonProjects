#working with urllib and BeautifulSoup

#pulling data from a url

#counting and summing numbers in a tag

import urllib.request, urllib.parse, urllib.error

import ssl

from bs4 import BeautifulSoup

sumlist = list()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


uurl = input('Enter your url:-')

ufhandle = urllib.request.urlopen(uurl, context = ctx).read()

souphandle = BeautifulSoup(ufhandle, 'html.parser')

#retrieving the span tags in the file and pulling out the number

tags = souphandle('span')

for tag in tags:
    nums = tag.contents[0]
    convt = int(nums)
    sumlist.append(convt)
    
print('Number count is:', len(sumlist))

print('Sum is:', sum(sumlist))







