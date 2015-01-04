#!/usr/bin/env python

from time import clock
from math import factorial

NUMBER = 100

def SolveViaBruteForce():
  return sum([ int(char) for char in str(factorial(NUMBER)) ])

def main():
  start = clock()
  print SolveViaBruteForce()
  print "cputime = " + str( clock() - start ) + " sec"

if __name__ == "__main__":
  main()