# Exercise 66 - Translator
# Question: Create an English to Portuguese translation program.
# The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.

d = dict(weather = "clima", earth = "terra", rain = "chuva")

print (d)
# Expected output:
#
# Enter word: earth
# terra

def translateP(word) :
    if word in d.keys():
        return (d[word])
    else :
        return ("No word in Dictionary!")

word = input("Enter word : ")
result = translateP(word)
print (result)

# print (word)
# if word in d.keys():
#     print (d[word])
# else :
#     print ("No word in Dictionary!")