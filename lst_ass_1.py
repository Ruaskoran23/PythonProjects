#list assignment one
#file name to be used is romeo.txt
#take file from user

#file created on 10/12/23 00:39

uinp = input('Please enter file name:')
fhandle = open(uinp)

#an empty list to store the split words
lst = list()
new_lst = list()

#splitting of line using loops#

for line in fhandle:
    lineall = line.rstrip()
    lst1 = lineall.split()
    for e in lst1:
        if e not in lst:
            lst.append(e)
            lst.sort()
print(lst)


