
def is_anagram_palindrome(word):
    """ write a function to determine if the anagram is indeed a palindrome."""

    # first we're given a word - test case: racecar - acerrca - True 
    # we want a boolean answer - T/F 
    # example palindromes:
        # racecar - only 1 e
        # noon - even number sets 
        # mom - only 1 o 
    # so basically there can only be one odd letter 
    # build a dictionary that stores the letter as the key and increments the value
    # then loop through the dictionary and return T/F if the letter count matches 
    # the above stipulation 

    palindrome_dict = {}

    # test case: bccb --> return True 

    for letter in word:
        count = palindrome_dict.get(letter, 0) # set var count to checking the dict for letter, else 0
        palindrome_dict[letter] = count + 1 # add letter as key, count + 1 as value

    see_odd = False # haven't seen an odd yet

    for count in palindrome_dict.count: # iterating by count in dict 
        if count % 2 != 0: # palidrome if odd count is 1 or 0
            return False
            see_odd = True

    return True 







