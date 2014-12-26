#!/usr/bin/env python
from time import clock
from math import sqrt, ceil

DIVISOR_TARGET = 500

def SolveViaBruteForce():
  number = 1
  count = 1
  while True:
    nDiv = 0
    div = 0
    while div <= int( ceil( sqrt( number ) ) ):
      div += 1
      if number % div == 0:
        nDiv += 2
    # correction if number is perfect square
    if int( sqrt( number ) ) * int( sqrt( number ) ) == number:
      nDiv -= 1
    if nDiv > DIVISOR_TARGET:
      return number
    count += 1
    number += count
    
def main():
  print SolveViaBruteForce()

if __name__ == "__main__":
  start = clock()
  main()
  print "cputime = " + str(clock() - start) + " sec"