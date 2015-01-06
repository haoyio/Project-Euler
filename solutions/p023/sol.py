#!/usr/bin/env python

from time import clock
from math import sqrt, ceil

SMALLEST_ABUNDANT_NUMBER = 12
UPPER_LIMIT = 28123

def SumProperDivisorsBruteForce(n):
  return sum( [ i for i in range( 1, n / 2 + 1 ) if n % i == 0 ] )

def GetAllAbundantNumbersBruteForce():
  abundantNumbers = []
  for i in range( SMALLEST_ABUNDANT_NUMBER, UPPER_LIMIT ):
    if SumProperDivisorsBruteForce(i) > i:
      abundantNumbers.append(i)
  return abundantNumbers

def GetSummedAbundantNumbers(abundantNumbers):
  canBeWrittenAsAbundant = [False] * ( UPPER_LIMIT + 1 )
  for i in abundantNumbers:
    for j in abundantNumbers:
      if i + j <= UPPER_LIMIT:
        canBeWrittenAsAbundant[ i + j ] = True
  return canBeWrittenAsAbundant

def SolveViaBruteForce():
  abundantNumbers = GetAllAbundantNumbersBruteForce()
  canBeWrittenAsAbundant = GetSummedAbundantNumbers(abundantNumbers)  
  return sum([ i for i in range(len(canBeWrittenAsAbundant)) \
               if not canBeWrittenAsAbundant[i] ])

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

def SumProperDivisors( n, primes ):
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

def GetAllAbundantNumbers():
  primes = GetPrimesUpTo(UPPER_LIMIT)
  abundantNumbers = []
  for i in range( SMALLEST_ABUNDANT_NUMBER, UPPER_LIMIT ):
    if SumProperDivisors( i, primes ) > i:
      abundantNumbers.append(i)
  return abundantNumbers

def SolveViaPrimeFactorization():
  abundantNumbers = GetAllAbundantNumbers()
  canBeWrittenAsAbundant = GetSummedAbundantNumbers(abundantNumbers)
  return sum([ i for i in range(len(canBeWrittenAsAbundant)) \
               if not canBeWrittenAsAbundant[i] ])

def main():
  start = clock()
  # print SolveViaBruteForce() # ~ 24 sec
  print SolveViaPrimeFactorization() # ~ 6 sec
  print "cputime = " + str( clock() - start ) + " sec"

if __name__ == "__main__":
  main()