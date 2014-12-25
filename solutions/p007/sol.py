#!/usr/bin/env python
from math import sqrt, ceil

DESIRED_COUNT = 10001

def SolveViaBruteForce():
  count = 1
  candidate = 2
  while count < DESIRED_COUNT:
    candidate += 1
    if IsPrime(candidate):
      count += 1
  return candidate

def IsPrime(x):
  if x == 2:
    return True
  elif x % 2 == 0:
    return False
  else:
    for j in range( 3, int( ceil( sqrt(x) ) ) + 1 ):
      if x % j == 0:
        return False
    return True

def main():
  print SolveViaBruteForce()

if __name__ == "__main__":
  main()