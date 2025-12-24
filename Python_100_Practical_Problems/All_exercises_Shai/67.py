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
    try :
        return (d[word])
    except KeyError :
        return ("No word in Dictionary!")

word = input("Enter word : ")
# result = translateP(word)
# print (result)
print (translateP(word))
