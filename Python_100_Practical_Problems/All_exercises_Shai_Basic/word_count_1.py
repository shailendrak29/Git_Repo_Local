# version 1 is the cleaner version of the code.
# pass the text file $1
# create a textfile-count as out put file
#
# output to have :
# total words :
# Unique words :
#
# word - count

import sys

# Read the input and decide the output file
if len(sys.argv) != 2 :
    print ("Incorrect number of arguments")
    sys.exit()
else :
    print (f"File to be processed is {sys.argv[1]}")

file = open (sys.argv[1],"r")
text = file.read()
file.close()

output_file = sys.argv[1][:-4]+"_count.txt"
print (f"Counts available in : {output_file}")

# print (f"Normal : {text.split()}")
# print (f"Lower : {text.split().lower()}")

# Perform the counts
word_count = {}
for word in text.split() :
    if word.lower() in word_count :
        word_count [word.lower()] +=1
    else :
        word_count [word.lower()] = 1
sorted_word_count = sorted(word_count.items() , key = lambda item : item[1], reverse = True)

# Print the values
file1=open(output_file,"w")
file1.write(f"\nTotal number of words : {len(text.split())}\nUnique words : {len(word_count)}\n\n Sorted Words : Counts")
for key1, value1 in sorted_word_count:    #way to loop list with tuple, no need of values
    file1.write(f"\n{key1} : {value1}")
file1.close()

print ("Word count completed !")