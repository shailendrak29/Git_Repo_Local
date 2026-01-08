# add missing countries in the countries_missing.txt . create new file


checklist = ['Portugal', 'Germany', 'Spain']
content = []

with open ("countries_missing.txt", "r") as f:
    content = f.readlines()

content = [ item.strip('\n') for item in content]
print (len(content))

# content.append([missing for missing in checklist if missing not in content ])
#
# print (len(content))
# print (content)

for missing in checklist :
    if missing not in content :
        content.append(missing)

print (len(content))
print (content)

content.sort() # sorts the list and returns None
print (content)
print (len(content))

with open ("countries_missing.txt","w") as f :
    f.seek(0)
    f.truncate()
    for data in content :
        f.write(data+'\n')

