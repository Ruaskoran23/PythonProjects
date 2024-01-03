#Tuple assignment

#reading from a file mboxshort.txt

#file created on 22/12/23 18:40

fname = input('Enter the name of the file:')

fhandle = open(fname)

count = dict()
#looping through the llines of files

for line in fhandle:
    if line.startswith('From '):
        words = line.split()
        for word in words:
            time = words[5]
            time_full = time.split(':')
            hours = time_full[0]
            count[hours] = count.get(hours, 0) + 1  #adds items to the dictionary if it isnt there

#creating a new list to accommodate the items

new = list()

#looping through the items of the dictionary

for key, val in count.items():
    new_pair = (key, val) #stores the key val in new_pair
    new.append(new_pair)

new = sorted(new)

#getting the ordered hours

for key,val in new:
    print(key, int(val/7))

            

