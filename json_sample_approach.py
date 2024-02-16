#json assignment practise

#using different approach to obtain the data

import json
import urllib.request, urllib.parse, urllib.error


jsonurl = input('Enter the json url:')

data = urllib.request.urlopen(jsonurl).read().decode()

#converting the json to python strings

jsondata = json.loads(data)

nulist = list()
namelist = list()

print('The length of the data is:', len(jsondata))

for item in jsondata['comments']:
    val = int(item['count'])
    name = item['name']
    nulist.append(val)
    namelist.append(name)

print(sum(nulist))
