name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
counts = dict()
handle = open(name)

#read file and count the number of appearance
for name in handle:
    name = name.rstrip()
    if not name.startswith('From '): continue
    words = name.split()
    #print(words[1])
    email = words[1]
    counts[email] = counts.get(email,0)+1

# compare and get the largest number
bigcount = None
bigword = None

for k,v in counts.items():
    if bigcount is None or v > bigcount:
        bigword = k
        bigcount = v
print(bigword, bigcount)
