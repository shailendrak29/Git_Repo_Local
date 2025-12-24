# Question:  What will the following script output? Please try to do this by mind if you can.

c = 1
def foo():
    return c
c = 3
print(foo())

#My answer : c is not defined in the function, so it should not print anything
#Actual answer : c value is global and function returns the latest value of c