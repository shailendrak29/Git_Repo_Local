# Question: Create a function that takes any string as input and returns the number of words for that string.

# import string

def str_len(line):
    return(len(line.split()))

a = "I am amazing"
print (str_len(a))
# line = "abc"
# print (len(line))

# print (list(a))
# print (a.split(" "))
# print (len(a.split(" ")))
