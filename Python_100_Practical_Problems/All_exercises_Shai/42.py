# Question: Print out in each line the sum of homologous items of the two sequences.

a = [1, 2, 3]
b = (4, 5, 6)
c = {"a":7,"b":8,"c":9}

# print (f"{len (a)} and {len(b)}")
# print (f"{a[1]} and {b[1]}")
# print (min(len(a),len(b)))
# print (a[1])

# for i in range(0,min(len(a),len(b))) :
#     print (f"{a[i]+b[i]}")
# print (zip(a,b, strict = True))

for i,j,k in zip(a,b,c.values(), strict = False):
    print (i+j+k)