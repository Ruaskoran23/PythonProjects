#json assignments

#extracting data from a URL that contains JSON

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

userinput = input('Enter your url link:')
userdata = urllib.request.urlopen(userinput, context=ctx).read().decode()
#loading of the json to python strings

jsinfo = json.loads(userdata)

print('The length of the data is:', len(jsinfo))


count = 0
total = 0

for item in jsinfo['comments']:
    count = count + 1
    total += int(item['count'])

print('The count is:', count)
print('The sum is:', total)

    
