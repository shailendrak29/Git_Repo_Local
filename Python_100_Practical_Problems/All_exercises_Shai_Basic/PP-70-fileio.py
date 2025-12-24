# file = open ("amazing.txt","w")
# file.write("Shailendra is amazing!")
# file.close()

# file1 = open("amazing.txt","r")
# print (file1.read())
# file1.close()

# file2 = open("amazing.txt","a+")
# file2.write("\nthis is 2nd new line")
# file2.seek(0)   # move pointer to beginning
# print(file2.read())
# file2.close()

file2 = open("amazing.txt","a+")
file2.write("\nthis is 11th new line")
file2.seek(0)   # move pointer to beginning
print(file2.read())
file2.seek(0)
file2.write("\nthis is 12th new line")
file2.close()


# need to be more comfortable with read write append and its cursor position