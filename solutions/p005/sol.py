#!/usr/bin/env python

MIN_INT = 1
MAX_INT = 20
RANGE = range( MIN_INT, MAX_INT + 1 )

def SolveViaBruteForce():
  '''
  Simply check all small positive numbers for even divisibility
  in RANGE.
  '''
  candidate = MAX_INT
  while not IsEvenlyDivisible(candidate, RANGE):
    candidate += MAX_INT
  return candidate

def IsEvenlyDivisible(x, numbers):
  '''
  Returns whether x is evenly divisible by all numbers in given
  number list. 
  '''
  for number in numbers:
    if x % number != 0:
      return False
  return True

def main():
  print SolveViaBruteForce()

if __name__ == "__main__":
  main()