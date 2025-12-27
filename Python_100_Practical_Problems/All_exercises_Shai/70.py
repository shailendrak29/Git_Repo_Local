# Exercise 70 - File from URL
# Question: Print out the text of this file https://pythonhow.com/media/data/universe.txt
# Don't manually download the file. Let Python do all the work.

import requests
url1 = 'https://pythonhow.com/media/data/universe.txt'

# print(*requests.get(url1))
response = requests.get(url1)
text = response.text
print (text)

help(response)

