#working with dictionaries
#reading from a file

#file created on 15/12/23 17:16

fname = input('Enter the name of the file:')
fhandle = open(fname)

counter = dict()

#looping through the line for words

for line in fhandle:
    if line.startswith('From:'):
        words = line.split()
        for word in words:
            email =  words[1]
            counter[email] = counter.get(email, 0) + 0.5


bigcount = None
bigword = None


for email,val in counter.items():
    if bigcount is None or val > bigcount:
        bigword = email
        bigcount = val

print(bigword, int(bigcount))
    
        
    
