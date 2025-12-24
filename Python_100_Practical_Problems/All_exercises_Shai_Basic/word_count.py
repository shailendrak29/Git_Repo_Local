# pass the text file $1
# create a textfile-count as out put file
#
# output to have :
# total words :
# Unique words :
#
# word - count

import sys
# import operator
print (len(sys.argv))
print (sys.argv[1])
if len(sys.argv) != 2 :
    print ("Incorrect number of arguments")
    sys.exit()
else :
    print (f"File to be processed is {sys.argv[1]}")

file = open (sys.argv[1],"r")
# print (file.read())
text = file.read()
file.close()

output_file = sys.argv[1][:-4]+"_count.txt"
print (f"Counts available in : {output_file}")

# print (text)
word_list = text.split()
# print (word_list)
print (f"\nTotal number of words : {len(word_list)}")
unique_list = set(word_list)
print (f"\nUnique words : {len(unique_list)}")
word_count = {}

for word in unique_list :
    word_count [word] =0
for word in word_list :
    word_count [word] +=1
# print (word_count)

print (f"total words via split : {len(text.split())}")
print (f"unique words dict : {len(word_count)}")

sorted_word_count = sorted(word_count.items() , key = lambda item : item[1], reverse = True)
print (sorted_word_count)
# this is a list of tuples

file1=open(output_file,"w")
file1.write(f"\nTotal number of words : {len(word_list)}\nUnique words : {len(unique_list)}\n\n Words : Counts")
# print ("\n\n Words : Counts")
# for key, value in word_count.items():     # way to loop a dictionary, use items
# #     print (f"\n {key} : {value}")
#     file1.write(f"\n{key} : {value}")


file1.write(f"\n\n Sorted Words : Counts")
for key1, value1 in sorted_word_count:    #way to loop list with tuple, no need of values
#     print (f"\n {key} : {value}")
    file1.write(f"\n{key1} : {value1}")

file1.close()