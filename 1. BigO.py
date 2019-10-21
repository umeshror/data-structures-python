#!/usr/bin/env python
# coding: utf-8

# # Big O Examples
#
# Let's begin with some simple examples and explore what their Big-O is.
#
#
#  O(1) Constant
#


def func_constant(values):
    '''
    Prints first item in a list of values.
    '''
    return values[0]


func_constant([1, 2, 3])


# Note how this function is constant because regardless of the list size,
#  the function will only ever take a constant step size, in this case 1,
#  printing the first value from a list. so we can see here that an input list
# of 100 values will print just 1 item, a list of 10,000 values will print just
# 1 item, and a list of **n** values will print just 1 item!

#
# O(n) Linear



def func_lin(lst):
    '''
    Takes in list and prints out all values
    '''
    for val in lst:
        print(val)


func_lin([1, 2, 3])


# This function runs in O(n) (linear time). T
# his means that the number of operations taking place scales linearly with n,
#  so we can see here that an input list of 100 values will print 100 times,
#  a list of 10,000 values will print 10,000 times, and a list of **n** values
# will print **n** times.

# ## O(n^2) Quadratic



def func_quad(lst):
    '''
    Prints pairs for every item in list.
    '''
    for item_1 in lst:
        for item_2 in lst:
            print item_1, item_2


lst = [0, 1, 2, 3]

func_quad(lst)


# Note how we now have two loops, one nested inside another.
# This means that for a list of n items, we will have to perform n operations
#  for *every item in the list!* This means in total, we will perform n times n
# assignments, or n^2. So a list of 10 items will have 10^2, or 100 operations.
#  You can see how dangerous this can get for very large inputs!
# This is why Big-O is so important to be aware of!

# ______
# ## Calculating Scale of Big-O
#
#
# When it comes to Big O notation we only care about the most significant terms,
# remember as the input grows larger only the fastest growing terms will matter.
#  If you've taken a calculus class before, this will reminf you of taking limits
#  towards infinity. Let's see an example of how to drop constants:



def print_once(lst):
    '''
    Prints all items once
    '''
    for val in lst:
        print val



print_once(lst)



# O(3n) == > O(n)
def print_3(lst):
    '''
    Prints all items three times
    '''
    for val in lst:
        print val

    for val in lst:
        print val

    for val in lst:
        print val


print_3(lst)




def comp(lst):
    '''
    This function prints the first item O(1)
    Then is prints the first 1/2 of the list O(n/2)
    Then prints a string 10 times O(10)
    '''
    print lst[0]

    midpoint = len(lst) / 2

    for val in lst[:midpoint]:
        print val

    for x in range(10):
        print 'number'



lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

comp(lst)
#O(1 + n/2 + 10) ===> O(n)

#


def matcher(lst, match):
    '''
    Given a list lst, return a boolean indicating if match item is in the list
    '''
    for item in lst:
        if item == match:
            return True
    return False


matcher(lst, 1)
#O(1)


matcher(lst, 11)
#O(n)

#
# ## Space Complexity
#


def printer(n=10):
    '''
    Prints "hello world!" n times
    '''
    for x in range(n):
        print 'Hello World!'


# O(1)
printer()



def create_list(n):
    new_list = []

    for num in range(n):
        new_list.append('new')

    return new_list


#O(n)

print create_list(5)

# * [Big-O Notation Explained](http://stackoverflow.com/questions/487258/plain-english-explanation-of-big-o/487278#487278)
#
# * [Big-O Examples Explained](http://stackoverflow.com/questions/2307283/what-does-olog-n-mean-exactly)
