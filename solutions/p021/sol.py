#!/usr/bin/env python

from time import clock
from math import sqrt, ceil

MAX_INT = 10000

def SumProperDivisors(n):
  return sum( [ i for i in range( 1, n / 2 + 1 ) if n % i == 0 ] )
  
def SolveViaBruteForce():
  total = 0
  for a in range( 1, MAX_INT + 1 ):
    da = SumProperDivisors(a)
    if a < da and da < MAX_INT: # check only a < b o.w. double-count
      dbCandidate = SumProperDivisors(da)
      if dbCandidate == a:
        total += a + da
  return total  
  
def main():
  start = clock()
  print SolveViaBruteForce()
  print "cputime = " + str( clock() - start ) + " sec"

if __name__ == "__main__":
  main()