my_range = range(1, 21)
print (list(my_range))
print ([x*10 for x in my_range])  #use list comprehension., square bracket is important
print (x*10 for x in my_range)  # this does not generate list, just the generator object id