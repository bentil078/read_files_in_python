fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for name in fh:
    name = name.rstrip()
    if not name.startswith('From '): continue
    words = name.split()
    count += 1
    print(words[1])

print("There were", count, "lines in the file with From as the first word")
