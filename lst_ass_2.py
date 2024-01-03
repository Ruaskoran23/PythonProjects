#assignment 2 on list
#reading from a file and working with list
#name of file is mbox-short.txt

#file created on 11/12/23 04:56

fname = input('Enter the name of the preferable file:')
fhandle = open(fname)

#using for loop to read lines from the file

count = 0

for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        ls = line.split()
        count = count + 1
        emails = ls[1]
        print(emails)
print("There were", count , "lines in the file with From as the first word")
    
