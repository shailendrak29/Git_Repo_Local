# Question:  Why is there an error in the code, and how would you fix it?
#
# def foo(a, b):
#     print(a + b)
#
# x = foo(2, 3) * 10

def foo(a, b):
    return a + b

# print (type(foo(2,3)))

x = foo(2, 3) * 10
print (x)

# Answer : Because foo does not return any value. I would be sending None, so none*10 will cause a type mismatch
# Solution return (a+b) result
# return a + b		Simple, clean
# return (a + b)		Redundant parentheses