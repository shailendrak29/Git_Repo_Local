# Question : Conditional extractor. Extract letters in string "python" from 26 text files and create a list out of them

import os
folder = "letters_dir"

content = []
# print (os.listdir(folder))
for file in os.listdir(folder) :
#     print (file)
    with open (folder+'/'+file, 'r') as f :
        value = f.read()
    if value in 'python' :
        content.append(value)
print (content)