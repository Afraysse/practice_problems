


    """ given an integer, print each digit in reverse order, starting with the ones place.

    TEST CASE: 1 --> print 1 
    TEST CASE: 314 --> print 4, 1, 3
    TEST CASE: 12 --> print 2, 1

    """

def print_nums(num):
    
    while num > 0:
        popped = num % 10 # should give us the remainder
        num = num / 10
        print popped 

print_nums(314) 

# OR

def print_nums(num):

    while not num % 10 == num:

        next_digit = num % 10
        print next_digit
        num = (num - next_digit) / 10

    print num


