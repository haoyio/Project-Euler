#!/usr/bin/env python

MIN_INT = 100
MAX_INT = 999

def SolveViaBruteForce():
  '''
  Brute force approach by checking all pairs of 3 digit numbers.
  '''
  largestPalindrome = 0
  for i in range( MIN_INT, MAX_INT + 1 ):
    for j in range( MIN_INT, MAX_INT + 1 ):
      candidate = i * j
      if IsPalindrome_r(str(candidate)) and \
         candidate > largestPalindrome:
        largestPalindrome = candidate
  return largestPalindrome

def IsPalindrome_r(x):
  '''
  Returns a boolean indicating whether x is a palindromic number.
  '''
  return x == x[::-1]

def main():
  print SolveViaBruteForce()

if __name__ == "__main__":
  main()