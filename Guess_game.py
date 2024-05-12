import random

def hangman():
    word_list = ["Amala", "Tuwo", "Afang", "Garri", "Ifokore"]
    random_number = random.randint(0, len(word_list)-1)
    chosen_word = word_list[random_number]
    guessed_word = ["_"] * len(chosen_word)
    attempts = 6

    print("Let's play Hangman!")
    print("Hint: The word is a local food in Nigeria.")
    print('_ ' * len(chosen_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("\nPlease guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter only one letter!")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a LETTER!")
        elif guess in guessed_word:
            print("You already guessed that letter!")
        elif guess not in chosen_word:
            print("Incorrect guess.")
            attempts -= 1
            print("You have", attempts, "attempts remaining.")
        else:
            print("Good guess!")
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    guessed_word[i] = guess
            print(' '.join(guessed_word))

    if "_" not in guessed_word:
        print("Congratulations, you won!")
    else:
        print("Sorry, you lost. The word was", chosen_word)

hangman()