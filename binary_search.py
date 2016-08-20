
def binary_search(num):
    """ 
    Binary search allows for searching of a sorted list in O(log n) time 
    by examining the middle item and if the sought-for value is smaller, move 
    halfway to the left. If larger, move halfway right. 

    """

    # the number best between 0 and 100
    assert 0 < num < 101 

    num_guesses = 0 

    # if we're searching for a number, we can assume to start at 50 

    higher_than = 0 
    lower_than = 101 
    guess = None 

    while guess != num:
        num_guesses += 1 
        # first round is 101 / 2 = 50 
        guess = (lower_than - higher_than) / 2 + higher_than

        if num > guess:
            higher_than = guess 

        elif num < guess:
            lower_than = guess 

    # number of guesses should never exceed 7
    return num_guesses

