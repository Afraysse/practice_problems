def _recursive_index(word, lst, start_at):

    """ 
    Look up a word in a lst using recursion and return the word.
    If the word isn't in the list, return None. 
    """

    # base case 

    if start_at == len(lst):
        return None

    # Have we found it?
    if lst[start_at] == word:
        return start_at

    return _recursive_index(word, lst, start_at + 1)

_recursive_index("needle", ["what", "needle", "why"], 0)
    