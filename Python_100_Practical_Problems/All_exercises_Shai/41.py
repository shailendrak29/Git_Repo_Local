# Question: Create a script that generates a text file with all letters of the English alphabet inside it, one letter per line.

import string

print (string.ascii_lowercase)

with open ("letters.txt","w") as f :
    for letter in string.ascii_lowercase :
        print (letter)
        f.write(letter + "\n")