def answer_found(inp_answer_word, inp_dict_letter):
    """
    Takes in word and guessed letters and returns True if answer is found
    :param inp_answer_word: Str answer word
    :param inp_dict_letter: Dict guessed letters are False
    :return: Boolean
    """
    for letter in inp_answer_word:
        remaining = 0
        if inp_dict_letter[letter]:
            remaining = remaining + 1
        if remaining > 0:
            return False
    # returns True if remaining stays at 0
    return True
