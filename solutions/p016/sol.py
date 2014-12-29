#!/usr/bin/env python

from time import clock

BIG_NUMBER = 2**1000

def SolveViaBruteForce():
  return sum( [ int(char) for char in str( BIG_NUMBER ) ] )

def main():
  print SolveViaBruteForce()

if __name__ == "__main__":
  start = clock()
  main()
  print "cputime = " + str( clock() - start ) + " sec"