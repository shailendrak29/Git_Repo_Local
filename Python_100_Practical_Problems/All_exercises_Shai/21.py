# Question: Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}

#dictionary comprehension

filter = {}

# filter[x]=y : x, y for d.items()
# filter[x]=y : for x, y in d.items()
filter = {x:y for x,y in d.items() if y<=1}
print (filter)

d = dict((key, value) for key, value in d.items() if value <= 1)
print (d)