print (i for i in range(1,21))  # this does not generate the list
print ([i for i in range(1,21)])  # having square bracket creates the list

# Just to print there is no need of for loop, just range is good enough
print (range(1,21))  # this gives object range. need list word to convert to list output
print (list(range(1,21)))  # this works
print (*range(1,21))
# The * unpacks the range into separate arguments.
# So this:                 print(*range(1, 21))
# becomes internally like: print(1, 2, 3, 4, ..., 20)