#regex assignment working with sample

#reading from a text file

import re

fname = input('Enter the name of the file:')

fhandle = open(fname)

numlist = list()

#looping through the lines to identify the number

for line in fhandle:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    if len(num) >=1:
        for val in num:
            numconvt = float(val)
            numlist.append(numconvt)
    
print(numlist)

print(len(numlist))
summation = sum(numlist)
print(summation)

