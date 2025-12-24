# Question : Extract letters from 26 text files and create a list out of them

import os
folder = "letters_dir"
#
# if not os.path.exists(folder):
#
#     os.makedirs(folder)
content = []
print (os.listdir(folder))
for file in os.listdir(folder) :
    print (file)
    with open (folder+'/'+file, 'r') as f :
        content.append(f.read())
#         files_content.append()
print (content)