# Exercise 71 - Letter Counter
# Question: Count the number of "a" characters in this text file: http://www.pythonhow.com/data/universe.txt

import requests, string
url1 = 'https://pythonhow.com/media/data/universe.txt'

# print(*requests.get(url1))
response = requests.get(url1)
# text = response.text
count_a = response.text.count("a")
print (count_a)


# print (help(text))

# count  = 0
#
# for chars in text :
#     print (chars)
#     if chars =='a' :
#         count = count+1
#
# # print (count)
