# Question: Create a script that generates a file where all letters of the English alphabet are listed three in each line. The inside of the text file would look like:
#
# abc
# def
# ghi
#
# and so on.

import string as s

print (s.ascii_lowercase)
print (s.ascii_lowercase[0::3])
print (s.ascii_lowercase[1::3])
print (s.ascii_lowercase[2::3])

file_name = "alphabets_3.txt"
# with open (file_name,"w") as f :
#     for i,j,k in zip (s.ascii_lowercase[0::3], s.ascii_lowercase[1::3],s.ascii_lowercase[2::3] , strict = False ) :
# #         print (i + j + k + "\n")
#         f.write(i + j + k + "\n")

# make it more readable and maintainable

letters = s.ascii_lowercase+" "
slice1 = letters[0::3]
slice2 = letters[1::3]
slice3 = letters[2::3]

with open (file_name,"w") as f :
    for s1,s2,s3 in zip(slice1, slice2, slice3, strict = False) :
        f.write(s1+s2+s3+"\n")
