# Question: Create a script that generates a file where all letters of the English alphabet are listed two in each line. The inside of the text file would look like:

# ab
# cd
# ef
#
# and so on.

import string
print (string.ascii_lowercase)
cnt=0
# for i,j in zip(string.ascii_lowercase[0::2],string.ascii_lowercase[1::2]) :
# #     if cnt%2 == 0 :
#
#     print (i+j)
# #     print (j)

file_name ="alphabets.txt"
with open (file_name, "w") as f:
    for i,j in zip(string.ascii_lowercase[0::2],string.ascii_lowercase[1::2]) :
        f.write (i+j+"\n")