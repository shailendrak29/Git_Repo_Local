# Exercise 59 - Enumerator
# Question: Please complete the code so that it prints out the expected output.

a = [1, 2, 3]
print (*enumerate(a))

for index, value in enumerate(a, start = 100) : # 100 just for fun 
    print (f'Item {value} has index {index}')
#
# for i in range (0,len(a)) :
#     print (f'Item {a[i]} has index {i}')

# Expected output:
#
# Item 1 has index 0
# Item 2 has index 1
# Item 3 has index 2