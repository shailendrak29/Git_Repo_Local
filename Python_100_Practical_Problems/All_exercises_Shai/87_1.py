checklist = ['Portugal', 'Germany', 'Spain']
content = []

with open ("countries_missing.txt", "r") as f:
    content = f.readlines()

print (content)
checklist = [item +'\n' for item in checklist]
print (checklist)

updated_content = sorted(content + checklist)
print (updated_content)

with open ("countries_missing_updated.txt","w") as f :
    for new_content in updated_content :
        f.write(new_content)