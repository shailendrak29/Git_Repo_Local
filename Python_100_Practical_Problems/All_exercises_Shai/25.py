#make a script that prints out letters of English alphabet from a to z

# for i in range('a','z') :
#     print (i)
#range is only for numbers
#
# for i in a..z :
#     print (i)

import string

for letter in string.ascii_lowercase:
    print (letter)

# string  is a built-in module and string.ascii_lowercase  returns a string object containing all 26 letters of the English alphabet. Then we simply iterate through that string and print out the string items.

print (string.ascii_lowercase)
# returns :
# abcdefghijklmnopqrstuvwxyz
