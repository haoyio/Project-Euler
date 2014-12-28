#!/usr/bin/env python

MAX_INT = 1000000

def IsEven( n ):
  return n % 2 == 0

def CollatzSucc( n ):
  if IsEven( n ):
    return n / 2
  else:
    return 3*n + 1

def CountSequence_r( n, cache ):
  if n in cache:
    return cache[ n ]
  else:
    cache[ n ] = CountSequence_r( CollatzSucc( n ), cache ) + 1
    return cache[ n ]

def SolveViaCaching():
  cache = { 1:1 }
  for i in range( 1, MAX_INT ):
    cache[ i ] = CountSequence_r( i, cache )
  return max( cache, key = cache.get )

def main():
  print SolveViaCaching()

if __name__ == "__main__":
  main()
