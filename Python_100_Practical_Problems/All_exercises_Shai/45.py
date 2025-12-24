# Question: Please create a script that generates 26 text files named a.txt, b.txt, and so on up to z.txt.
# Each file should contain a letter reflecting its filename. So, a.txt will contain letter a, b.txt will contain letter b, and so on.

import string as s, os
# from os import makedirs

letters = s.ascii_lowercase
print (letters)
folder_name = "letters_dir2"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

for value in letters :
    file_name = value+".txt"
#     print (file_name)
    with open (folder_name+"/" + file_name,"w") as f :
        f.write(value)