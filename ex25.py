def break_words(parameter):
    """This function will break up words for us."""
    words = parameter.split(' ')
    return words

def sort_words(parameter):
    """Sorts the words."""
    return sorted(parameter)

def print_first_word(parameter):
    """Prints the first words after popping it off."""
    word = parameter.pop(0)
    print(word)

def print_last_word(parameter):
    """Prints the last word after popping it off."""
    word = parameter.pop(-1)
    print(word)

def sort_sentence(parameter):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(parameter)
    return sort_words(words)

def print_first_and_last(parameter):
    """Prints the first and last words of the sentence."""
    words = break_words(parameter)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(parameter):
    """Sorts the words then prints the first and last ones."""
    words = sort_sentence(parameter)
    print_first_word(words)
    print_last_word(words)