# Question: The following script throws a NameError  in the last line saying that c  is not defined. Please fix the function so that there is no error and the  last line can print out the value of c  (i.e. 1 ).

def foo():
    global c
    c = 1
    return c
foo()
print(c)

# my answer was c = foo()
# actual answer/ smarter answer to make c global within the function
# Adding global c  fixes the code. That line makes available name c  in the global namespace. Therefore,  print can access the variable c .