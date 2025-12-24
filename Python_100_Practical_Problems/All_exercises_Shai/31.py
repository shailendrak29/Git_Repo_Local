# Question:  Why is there an error in the code, and how would you fix it?

def foo(a=1, b=2):
    return a + b

# x = foo - 1
x = foo() - 1
print (x)
print(type(foo()))
# parenthisis were missing while calling the function.