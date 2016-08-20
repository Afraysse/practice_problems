
def count_list_recursively(lst):
    """ count all the items in a list recursively. """

    # base case 
    count = 0

    if len(lst) <= 0:
        return count

    else: 
        count += 1 
        return count + count_list_recursively(lst[1:])

count_list_recursively([2, 3, 4])

# with test case, should return 3

# OR 

def count_list_recursively(lst):

    if not lst:
        return 0 

    else:
        return 1 + count_list_recursively(lst[1:])