# Exercise 57 - JSON to Dictionary
# Question: Please download the file in the attachment and use Python to print out its content.

import json, pprint

with open ("emp.json","r") as f:
#     print (f.read())
    d = json.loads(f.read())
pprint.pprint (d)
print (d)