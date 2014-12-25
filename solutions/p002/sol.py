#!/usr/bin/env python


MAX_INT = 4000000
FIRST_INT = 1
SECOND_INT = 2


def SumViaSkipTwo():
  '''
  Observe that successive even numbers in Fibonacci sequence have
  a gap of two after 2. (Proof is easy by considering parity of 
  first two numbers in the sequence and definition of sequence.)
  Thus, we can simply generate and add them as we go to the number
  smaller or equal to 4 million.
  '''
  prevInt = FIRST_INT
  currEvenInt = SECOND_INT
  total = 0
  while currEvenInt <= MAX_INT:
    total += currEvenInt
    firstOddInt = prevInt + currEvenInt
    secondOddInt = currEvenInt + firstOddInt
    currEvenInt = firstOddInt + secondOddInt
    prevInt = secondOddInt
  print total


def main():
  SumViaSkipTwo()


if __name__ == "__main__":
  main()