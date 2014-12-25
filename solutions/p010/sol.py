#!/usr/bin/env python
from math import sqrt, ceil

MAX_INT = 2000000

def SolveViaBruteForce():
  total = 2
  candidate = 3
  while candidate < MAX_INT:
    if IsPrime(candidate):
      total += candidate
    candidate += 2
  return total

def IsPrime(x):
  if x == 2:
    return True
  elif x % 2 == 0:
    return False
  else:
    for j in range( 3, int( ceil( sqrt(x) ) ) + 1, 2 ):
      if x % j == 0:
        return False
    return True

def main():
  print SolveViaBruteForce()

if __name__ == "__main__":
  main()