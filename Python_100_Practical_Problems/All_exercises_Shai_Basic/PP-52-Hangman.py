# Hangman game implementation

lives  = 5
word = "Fantastic"  # The word to guess, can be changed
word_list = list(word.lower())
guessed_word = ["_"] * len(word_list)


def hangman():
    global lives
    while lives > 0 and "_" in guessed_word:
        print("Current word: ", " ".join(guessed_word))
        print(f"Lives left: {lives}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in word_list:
            for index, letter in enumerate(word_list):
                if letter == guess:
                    guessed_word[index] = guess
            print("Good guess!")
        else:
            lives -= 1
            print("Wrong guess!")

    if "_" not in guessed_word:
        print("Congratulations! You've guessed the word:", word)
    else:
        print("Game over! The word was:", word)


hangman()