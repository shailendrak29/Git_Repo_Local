# Question: Make a script that prints out numbers from 1 to 10
#
# Expected output:
#
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

print("using basic for loop")
for number in range(1,11) :
    print (number)

print ("using comprehension \n")
[print(i) for i in range (1,11)]

print ("directly using range, unpack and separator")
print (*range(1,11),sep="\n")