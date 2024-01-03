#working with for loops and while loops
##starting with while loops

#file created on 21/11/23 08:24

smallest = None
largest = None

while True:
    num = input("Enter a number:")
    if num == "done":
              break     #it takes code to the end of loop
    try:                #basically this will give an error with a string entered, try will tell it to ignore
        fval = int(num)
    except:
           print("Invalid input")
           continue #conditions should always come after continue
           
    if smallest is None and largest is None:
              smallest = fval
              largest = fval
    elif fval < smallest:
              smallest = fval
    elif fval > smallest and fval < largest:
              smallest = fval
    elif fval > largest:
              largest = fval
    

print("Maximum is", largest)
print("Minimum is", smallest)
