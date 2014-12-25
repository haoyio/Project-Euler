#!/usr/bin/env python


MAX_INT = 1000
BASE1 = 3
BASE2 = 5


def SolveViaBruteForce():
  '''
  Solves by enumerating all integers between 1 and MAX_INT
  and checking their modulo for divisibility by the BASEs.
  '''
  total = 0
  for i in range(MAX_INT):
    if i % BASE1 == 0 or i % BASE2 == 0:
      total += i
  print total


def main():
  SolveViaBruteForce()


if __name__ == "__main__":
  main()