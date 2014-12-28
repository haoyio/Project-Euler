#!/usr/bin/env python

from time import clock
from math import sqrt, ceil
from collections import Counter
from operator import mul

DIVISOR_TARGET = 500
LARGE_NUMBER = 75000

def GetNumberOfDivisorsViaBruteFoce(number):
  '''
  Simply checks all integers up to |number| if they are divisors.
  Simple improvement of skipping the dual divisor greater than
  the square root of |number|.
  '''
  nDiv = 0
  div = 0
  while div <= int( ceil( sqrt( number ) ) ):
    div += 1
    if number % div == 0:
      nDiv += 2
  # correction if number is perfect square
  if int( sqrt( number ) ) * int( sqrt( number ) ) == number:
    nDiv -= 1
  return nDiv

def SolveViaBruteForce():
  number = 1
  count = 1
  while GetNumberOfDivisorsViaBruteFoce( number ) < DIVISOR_TARGET:
    count += 1
    number += count
  return number
    
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
    primes = []
    for i in range( len( primesBool ) ):
      if primesBool[i] == True:
        primes.append( i )
    return primes
  
def GetNumberOfDivisorsViaPrimeFactorization( x, primes ):
  '''
  Returns the number of divisors for |x|, given a large list of
  prime numbers. The idea is that given |x|'s prime factor list 
  and its corresponding exponents, we can find how many divisors
  there are by computing how many different combinations there are 
  that the prime factors can be multiplied with each other, up to 
  the number of times equal to each of the prime factors' 
  exponents. 
  '''
  numDivisors = 1
  for i in range( len( primes ) ):
    if primes[i] ** 2 > x:
      return 2 * numDivisors
    exp = 1
    while x % primes[i] == 0:
      exp += 1
      x /= primes[i]
    numDivisors *= exp
    if x == 1: # return count if can't further divide number
      return numDivisors
  return numDivisors

def SolveViaPrimeFactors():
  '''
  Check each triangle number by finding its number of divisors
  using the number of ways its prime factors can be multiplied.
  '''
  number = 1
  count = 1
  primes = GetPrimesUpTo( LARGE_NUMBER )
  while GetNumberOfDivisorsViaPrimeFactorization( number, primes ) \
        < DIVISOR_TARGET:
    count += 1
    number += count
  return number

def main():
  # print SolveViaBruteForce() # ~26 sec
  print SolveViaPrimeFactors() # ~1.4 sec

if __name__ == "__main__":
  start = clock()
  main()
  print "cputime = " + str(clock() - start) + " sec"