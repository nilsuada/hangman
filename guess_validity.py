def guess_is_valid(inp_dict_letters, inp_guess_character):
    """
    Checks if guess is a valid character and has not been guessed previously
    :param inp_dict_letters: Dict
    :param inp_guess_character: String
    :return: Boolean
    """

    if inp_guess_character not in inp_dict_letters.keys():
        # chekcs if guess is a valid character
        print("You have not entered a valid character.")
        return False

    if inp_dict_letters[inp_guess_character]:
        # checks if guess has been previously used and updates the dict
        inp_dict_letters[inp_guess_character] = False
        return True

    else:
        # returns false if the guess has been previously guessed
        print("You have guessed this character before.")
        return False
