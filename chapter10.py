name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
lst = list()
#read file and count the number of appearance
for name in handle:
    name = name.rstrip()
    if not name.startswith('From '): continue
    words = name.split()
    
    # use slicing to get just the hours from the time
    hours = words[5].split(':')
    hour = hours[0]
    counts[hour] = counts.get(hour,0)+1

#loop through the dictionary items as tuples and append to a list    
for key,val in counts.items():
    newtup = (key, val)
    lst.append(newtup)

# sort the list items   
# lst = sorted(lst)

# print sorted items
for k, v in sorted(lst):
    print(k,v)

