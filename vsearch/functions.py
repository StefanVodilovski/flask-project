
def search_for_letters(phrase:str, letters:str) -> set:
    """ returns letters from a word"""
    return set(letters).intersection(set(phrase))
