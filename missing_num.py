
""" 
SOLUTION 1: Simple Solution - O(N)
keep track of what you've seen in a seperate list. 

"""

def find_missing_num(nums, max_num):

    # find what number is missing from the list and return it 
    # there's a way of solving in O(n), but can also solve in O(log N)
    # list may be in any order 

    seen = [False] * max_num

    for n in nums:
        seen[n - 1] = True

    # the false value is the one not yet seen 

    return seen.index(False) + 1

# SOLUTION RUNTIME: O(N) and requires additional storage -- not ideal 

"""
SOLUTION 2: Sorting Solution - O(N log N)

Sort the numbers first, then scan thme to see which one missing. 
"""

def misisng_num(nums, max_num):

    nums.append(max_num + 1) # adds one larger than the max
    nums.sort() # sorts list to make more iterable 
    last = 0 

    for i in nums:
        if i != last + 1:
            return last + 1 

        last += 1 

    raise Exception("None are missing!")

""" SOLUTION 3: add the numbers and subtract from expected sum. """

def missing_num(nums, max_num):

    expected = sum(range(max_num + 1))

    return expected - sum(nums)

    # will return the missing number 










