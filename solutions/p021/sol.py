#!/usr/bin/env python

from time import clock
from math import sqrt, ceil

MAX_INT = 10000

def SumProperDivisors(n):
  return sum( [ i for i in range( 1, n / 2 + 1 ) if n % i == 0 ] )
  
def SolveViaBruteForce():
  total = 0
  for a in range( 1, MAX_INT + 1 ):
    da = SumProperDivisors(a)
    if a < da and da < MAX_INT: # check only a < b o.w. double-count
      dbCandidate = SumProperDivisors(da)
      if dbCandidate == a:
        total += a + da
  return total

def GetPrimesUpTo(x):
  '''
  Returns a list of prime numbers up to |x| via the sieve of 
  Eratosthenes.
  '''
  if x < 2:
    return None
  else:
    primesBool = [True] * ( x + 1 )
    primesBool[0] = False
    primesBool[1] = False
    for i in range( 2, int(ceil( sqrt( x ) ) ) + 1 ):
      if primesBool[i] == True:
        j = i**2
        while j <= x:
          primesBool[j] = False
          j += i
    return [ i for i in range(len(primesBool)) if primesBool[i] ]

def SumProperDivisorsViaPrimeFactors( n, primes ):
  '''
  Returns the sum of proper divisors using the divisor function.
  '''
  nCopy = n
  netSum = 1
  primeIdx = 0
  prime = primes[primeIdx]
  nPrimes = len(primes)
  while prime**2 <= nCopy and nCopy > 1 and primeIdx < nPrimes:
    prime = primes[primeIdx]
    primeIdx += 1
    if nCopy % prime == 0:
      j = prime**2
      nCopy /= prime
      while nCopy % prime == 0:
        j *= prime
        nCopy /= prime
      netSum *= ( j - 1 ) / ( prime - 1 )
  # a prime factor larger than the square root remains
  if nCopy > 1:
    netSum *= nCopy + 1
  return netSum - n
  
def SolveViaPrimeFactorization():
  primes = GetPrimesUpTo(MAX_INT)
  total = 0
  for a in range( 1, MAX_INT + 1 ):
    da = SumProperDivisorsViaPrimeFactors( a, primes )
    if a < da and da < MAX_INT: # check only a < b o.w. double-count
      dbCandidate = SumProperDivisorsViaPrimeFactors( da, primes )
      if dbCandidate == a:
        total += a + da
  return total

def main():
  start = clock()
  # print SolveViaBruteForce() # ~3 sec
  print SolveViaPrimeFactorization() # ~0.07 sec
  print "cputime = " + str( clock() - start ) + " sec"

if __name__ == "__main__":
  main()