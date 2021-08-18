import re

# Handle the file import
name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1338408.txt"
handle = open(name)

#declare a list to handle numbers
numberlist = list()

#loop through the numbers and add them to list
for line in handle:
    line = line.rstrip()
    number = re.findall('[0-9]+', line)
    
    #skip empty strings
    if len(number) < 1: continue

    #convert all numbers in individual list to an integer
    number = [int(i) for i in number]

    #add individual list to numberlist
    for n in number:
        numberlist.append(n)

print(numberlist)
print(sum(numberlist))
