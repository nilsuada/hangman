import random_word
import hide
import guess_validity
import game_complete
import guess_in_word


def hangman_game():

    # Str - the answer the user will try to guess:
    answer_word = random_word.generate_random_word()
    # Dict - guessed characters are False:
    letters_dict = {
        "a": True,
        "b": True,
        "c": True,
        "d": True,
        "e": True,
        "f": True,
        "g": True,
        "h": True,
        "i": True,
        "j": True,
        "k": True,
        "l": True,
        "m": True,
        "n": True,
        "o": True,
        "p": True,
        "q": True,
        "r": True,
        "s": True,
        "t": True,
        "u": True,
        "v": True,
        "w": True,
        "x": True,
        "y": True,
        "z": True
    }
    # Int - number of guesses left
    num_of_guesses_left = 10
    # Str - instructions to print first time
    instructions = """Welcome to Hangman!
You must enter lower case letters only. 
Goodluck!"""

    print(instructions)

    # loop that runs while there are guesses left and answer is not found
    while num_of_guesses_left > 0 and not game_complete.answer_found(answer_word, letters_dict):

        print(hide.display_word(answer_word, letters_dict))
        print("You have", num_of_guesses_left, "guesses left.")
        input_guess = str(input("Enter a lowercase character to guess: "))

        # checks if guess is valid, updates dict if correct, and runs code
        if guess_validity.guess_is_valid(letters_dict, input_guess):

            #checks if guess is in answer and if True runs code
            if guess_in_word.guess_correct(answer_word, input_guess):
                print("Your guess is in the answer.")

            else:
                print("Your guess is not in the answer. You have lost a guess.")
                num_of_guesses_left = num_of_guesses_left - 1

        # if the guess is not valid the while loop will repeat without losing a guess

    if game_complete.answer_found(answer_word, letters_dict):
        print("Congratulations! You have guessed the word " + answer_word + " correctly.")
    else:
        print("You have run out of guesses. The correct answer was: " + answer_word + ".")


hangman_game()