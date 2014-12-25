#!/usr/bin/env python

MAX_INT = 100

def SolveViaBruteForce():
  '''
  Simply take the difference...
  '''
  squareOfSum = ( MAX_INT*( MAX_INT + 1 )/2 )**2
  sumOfSquare = ( MAX_INT*( MAX_INT + 1 )*( 2*MAX_INT + 1 ) )/6
  return abs( sumOfSquare - squareOfSum )

def main():
  print SolveViaBruteForce()

if __name__ == "__main__":
  main()