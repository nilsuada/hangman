def display_word(inp_answer, inp_letter_dict):
    """
    Takes string and if letters have been guessed and returns new string with only guessed letters shown
    :param inp_answer: String (word to change)
    :param inp_letter_dict: Dict (has string been guessed)
    :return: String
    """
    return_word = ""
    for letter in inp_answer:
        if inp_letter_dict[letter]:
            return_word = return_word + "_"
        else:
            return_word = return_word + letter
    return return_word
