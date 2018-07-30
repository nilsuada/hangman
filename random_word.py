import random


def generate_random_word():
    """
    Function that takes no input and returns a randomly generated word from list of words
    :return: String
    """
    # list of random words that the word will be generated from
    list_of_words = [
        "silicon",
        "valley",
        "baby",
        "dalmatian",
        "pineapple",
        "ubuntu",
        "incubator",
        "stream",
        "mountain",
        "garage",
        "bananas",
        "startup",
        "glasses",
        "orbit",
        "horror",
        "accident",
        "locksmith",
        "orange",
        "prospect",
        "diamond",
        "placebo",
        "data",
        "database"
    ]

    random_number = random.randint(0, len(list_of_words))
    return list_of_words[random_number]
