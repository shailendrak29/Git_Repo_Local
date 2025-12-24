# Hangman game : Provide a Word . The player to should, identify the word.
# for each incorrect guess the lives will be reduced

lives = 5
word = "Fantastic"
to_guess = len(word)*['_']
print(to_guess)
word_list = list(word.lower())
print (word_list)

while lives > 0 and '_' in to_guess :
    print (f"Lives remaining are {lives}")
    print ("Guessed word : "," ".join(to_guess))    # a space is joined between each alphabet of the new word
    # print("CHeck word :".join(to_guess))
    entry = input("Enter the alphabet : ").lower()

    if len (entry) > 1 or not entry.isalpha():
        print ("Enter valid one letter!!")
        continue
    elif entry in to_guess :
        print ("Already entered letter, enter a different letter")
        continue

    if entry in word_list :
        # print("Correct entry ")
        for index, value in enumerate(word_list):
            if value == entry :
                to_guess[index] = entry
        print ("Correct Guess")
    else :
        print ("incorrect entry")
        lives -= 1

if lives > 0 and '_' not in to_guess :
    print("Congratulation letter identied :"," ".join(to_guess))
else :
    print ("Lost the game")