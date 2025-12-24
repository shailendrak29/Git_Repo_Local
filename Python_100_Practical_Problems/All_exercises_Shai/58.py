# Exercise 58 - Add to JSON
# Question: Please download the json file in the attachment and use Python to add a new employee to the file's content so that the file looks like in the expected output below.

# possible solution
# one way is read all , append one to dictionary and push all - not feasible for huge data content.should have something like appen

import json

with open ("emp_ope.json" , "r+") as f :
#     d = json.loads(f.read())
#     print (d)
#     print (type (d))
#     d['employees'].append({"firstName":"Shail", "lastName" : "Kelk"})
#     print (d)
    f.seek(10)
#     json.dump(d,f,indent = 4)
    f.truncate()