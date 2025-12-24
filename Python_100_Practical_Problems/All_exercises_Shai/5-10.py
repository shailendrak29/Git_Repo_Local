#exercises 5 to 10 - all are sequence / slice based

letters = ["a","b","c","d","e","f","g","h","i","j"]
#5
print(letters[1])
#6
print (letters[3:6]) # slicing syntax is upper-bound exclusive, we need to pass 6  as the upper bound.
#7
print(letters[:3])
# or
print(letters[0:3])
#8
print(letters[-2])
#9
print (letters[-3:]) #  When you don't put any index to the colon's right, everything is included, and upper-bound exclusivity is ignored.
#10
print (letters[::2]) # The complete syntax of list slicing is [start:end:step] .
#When you don't pass a step, Python assumes the step is 1. [:]  itself means to get everything from start to end.

new_letter = []
for a in range(len(letters)) :
    if a%2 == 0 :
#         b = int(a/2)
#         new_letter[int(a/2)] = letters[a]
#         new_letter[b]=letters[a]
        new_letter.append(letters[a])
print (new_letter)

print (letters[::2])  # start : end : step