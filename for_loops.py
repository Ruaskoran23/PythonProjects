#working with for loops
#exploring perosnal data

#file created on 21/11/23 19:45

count = 0
tot = 0

for var in [20, 10, 15, 5, 3, 4, 12]:
    count = count + 1
    tot = tot + var
    print(var, tot)
print("The Count and total is:", count, tot)
print("The average here is:", tot/count)
