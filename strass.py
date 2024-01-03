#assignment with strings
#reading and working with strings
#assignment to read file and perform calculations
#file name is mxbox_short.txt

#file created on 04/12/23

#taking the user input of the file name
file1 = input("Please enter your file names:")
file2 =  open(file1)
count = 0
step4 = 0
for line in file2:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        step1 = line.find(' ')
        step2 = line[step1 + 1: 27]
        step3 = float(step2)
        step4 = step3 + step4
        step5 = step4 / count
print("The average spam confidence:", step5)
