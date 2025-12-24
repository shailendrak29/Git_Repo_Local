#Question: Calculate the sum of all dictionary values.

d = {"a": 1, "b": 2, "c": 3}

print(d)
print (d.values())
print (sum(d.values()))
# sum =0
# for i in d.values() :
#     sum += i
# print (sum)
#

d.values()  returns a list-like dict_values object while the sum function calculates the sum of the dict_values  items.