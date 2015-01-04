#!/usr/bin/env python

from time import clock

SMALLEST_ABUNDANT_NUMBER = 12
UPPER_LIMIT = 28123

def SumProperDivisors(n):
  return sum( [ i for i in range( 1, n / 2 + 1 ) if n % i == 0 ] )

def GetAllAbundantNumbers():
  abundantNumbers = []
  for i in range( SMALLEST_ABUNDANT_NUMBER, UPPER_LIMIT ):
    if SumProperDivisors(i) > i:
      abundantNumbers.append(i)
  return abundantNumbers

def SolveViaBruteForce():
  abundantNumbers = GetAllAbundantNumbers() # ~17 sec--too slow
  total = 0
  # TODO
  return total

def main():
  start = clock()
  print SolveViaBruteForce()
  print "cputime = " + str( clock() - start ) + " sec"

if __name__ == "__main__":
  main()