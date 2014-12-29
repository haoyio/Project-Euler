#!/usr/bin/env python

from time import clock
from math import factorial

SIDE_NODES = 20

def NoPathLeft( row, col ):
  return row > SIDE_NODES or col > SIDE_NODES

def IsLastNode( row, col ):
  return row == SIDE_NODES and col == SIDE_NODES

def CountPaths_r( row, col ):
  if IsLastNode( row, col ):
    return 1
  elif NoPathLeft( row, col ):
    return 0
  else:
    return CountPaths_r( row + 1, col ) + \
           CountPaths_r( row, col + 1 )

def SolveViaBruteForce():
  return CountPaths_r( 0, 0 )

def nCr( n, r ):
  f = factorial
  return f( n ) / f( r ) / f( n - r )

def SolveViaCombination():
  return nCr( SIDE_NODES * 2, SIDE_NODES )

def main():
  # print SolveViaBruteForce()
  print SolveViaCombination()

if __name__ == "__main__":
  start = clock()
  main()
  print "cputime: " + str( clock() - start ) + " sec"