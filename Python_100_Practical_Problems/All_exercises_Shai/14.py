# set
# OrderedDict
# append

# set : this creates unique but does not preserve the order

a = ["1", 1, "1", 2]
print (list(set(a)) )

# OrderedDict

from collections import OrderedDict
print(OrderedDict.fromkeys(a))
print(list(OrderedDict.fromkeys(a)))

# append

a = ["1", 1, "1", 2]
b = []
for i in a :
    if i not in b :
        b.append(i)
print (b)