#!/usr/bin/env python

from time import clock

FIB_1 = 1
FIB_2 = 1
MIN_INT = 10**(1000 - 1)

def brute_force_solution():
    prev_number = FIB_1
    curr_number = FIB_2
    counter = 2
    while curr_number < MIN_INT:
        new_number = curr_number + prev_number
        prev_number = curr_number
        curr_number = new_number
        counter += 1
    return counter

def main():
    start = clock()
    print brute_force_solution()
    print "cputime = " + str(clock() - start) + " sec"

if __name__ == "__main__":
    main()