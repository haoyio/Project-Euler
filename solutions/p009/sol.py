#!/usr/bin/env python

SUM = 1000

def SolveViaBruteForce():
  for a in range( SUM ):
    for b in range( a + 1, SUM ):
      for c in range( b + 1, SUM ):
        if a + b + c == SUM and a**2 + b**2 == c**2:
          return a*b*c

def main():
  print SolveViaBruteForce()

if __name__ == "__main__":
  main()