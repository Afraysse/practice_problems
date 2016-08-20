
def decode_string(s):

    """ 
    A valid code is a sequence of nums and letters, always starting with 
    a number and ending with a letter(s). Skip the number of letters according
    to the number preceeding. 

    Test Case: '0h1ae2bcy' --> 'hey'

    """

    # several options for solving 
    # could iterate over the string and store the desirable letters 
    # in a list, then use a "".join() to convert to a string 
    # we know that the first i will be number 

    word = ""
    i = 0 # as indexing for both nums and letters

    # use a while loop because we'll be indexing 
    while i < len(s):

        skip = int(s[i]) # first round: skip = 0
        i += skip + 1 
        word += s[i] 

        i += 1 

    return word 

decode_string("1eh0e2rvy")


