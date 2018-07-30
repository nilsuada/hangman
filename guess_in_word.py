def guess_correct(inp_answer_word, inp_guess_letter):
    """
    Checks if guess is in answer and returns True if it is
    :param inp_answer_word: Str answer
    :param inp_guess_letter: Str guessed letter
    :return: Boolean
    """
    if inp_guess_letter in inp_answer_word:
        return True
    else:
        return False