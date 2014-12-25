#!/usr/bin/env python
from math import sqrt

TARGET = 600851475143

def SolveViaBruteForce(x):
  '''
  Just check all possible prime factors up to square root of
  TARGET. Returns TARGET if no prime factor found.
  '''
  tgtSqrt = int(round(sqrt(x)))
  primeFactor = 0
  for i in range(1, tgtSqrt + 1):
    if x % i == 0 and IsPrime(i):
      primeFactor = i
  if primeFactor == 0:
    return x
  else:
    return primeFactor

def IsPrime(x):
  if x == 2:
    return True
  elif IsEven(x):
    return False
  else:
    for j in range(3, int(sqrt(x))):
      if x % j == 0:
        return False
    return True

def IsEven(x):
  return x % 2 == 0

def main():
  print SolveViaBruteForce(TARGET)

if __name__ == "__main__":
  main()