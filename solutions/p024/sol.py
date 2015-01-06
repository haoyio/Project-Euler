#!/usr/bin/env python

from time import clock
from math import factorial

DESIRED_POSITION = 1000000

def counting_solution():
    '''
    Observe that we can find the exact number by simply counting
    the number of permutations within a range of permutations
    with 9, 8,..., and finally 1 digit(s). E.g., we know that 
    the first digit must be 2 since we need at least the 3rd
    permutation of the last 9 digits in order to get over a 
    million possible permutations. From this insight, we can
    find the rest of the digits using the same procedure.
    '''
    numbers = [i for i in range(10)]
    remain = DESIRED_POSITION - 1
    perm = []
    for i in list(reversed(range(10))):
        fact = factorial(i)
        div = remain / fact
        perm.append(numbers[div])
        del numbers[div]
        remain -= div * fact
    return ''.join(map(str, perm))

def main():
    start = clock()
    print counting_solution()
    print "cputime = " + str(clock() - start) + " sec"

if __name__ == "__main__":
    main()
