# Question: Create a function that takes a text file as input and returns the number of words contained in the text file.
# Please take into consideration that a comma can separate some words with no space.
# For example, "Hi, it's me." would need to be counted as three words. For your convenience, you can use the text file in the attachment

import re

file_path ="D:\\Shailendra Kelkar\\Projects\\My_Git_Repo\\Python_100_Practical_Problems\\resources\\words2.txt"

with open(file_path,"r") as f:
    content = f.read()
    print (content)
    print ("basic : ")
    print(content.split())
    print ("1st : ")
    print (re.split(",| ", content) ) # regular expression split comma or space
    print ("2nd : ")
    print (re.split(r"[ ,]", content))
    print ("3rd : ")
    print (re.split(r"[,\s]", content)) # Use \s (any whitespace: space, tab, newline):
    print ("4th : ")
    print (re.split(r"[,\s]+", content)) # + for one or more, but still same result
    print ("5th : ")
    print (re.findall(r"\b\w+\b", content)) # cleanest \b is word boundary at start and end of \1 which is word consisting of
    #     letters: a–z, A–Z
    #     digits: 0–9
    #     underscore _
    #     + means: one or more
