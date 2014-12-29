#!/usr/bin/env python

from time import clock

SUM_1_9 = 36
SUM_10_19 = 70
SUM_20_99 = 10*( 6 + 6 + 5 + 5 + 5 + 7 + 6 + 6 ) + 8*SUM_1_9
#           tens                                   ones
SUM_1_99 = SUM_1_9 + SUM_10_19 + SUM_20_99
SUM_100_999 = 100*SUM_1_9 + 9*SUM_1_99 + 9*7 +     9*99*10
#             ones                       "hundred" "hundred and"
SUM_1000 = 11

def SolveViaPatternRecognition():
  return SUM_1_99 + SUM_100_999 + SUM_1000

def main():
  print SolveViaPatternRecognition()

if __name__ == "__main__":
  start = clock()
  main()
  print "cputime = " + str( clock() - start ) + " sec"