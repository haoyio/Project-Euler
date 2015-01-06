#!/usr/bin/env python

from time import clock

NAMES_FILENAME = 'p022_names.txt'

def GetSortedNames(filename):
  '''
  Reads in the file with file name |filename| and returns a sorted
  list of names in the file.
  '''
  textFile = open( filename, 'r' )
  names = textFile.read().split('","')
  names[0] = names[0].strip('"')
  names[-1] = names[-1].strip('"')
  names.sort()
  return names

def SolveViaBruteForce(names):
  totalNameScores = 0
  for nameIdx in range(len(names)):
    namePosition = nameIdx + 1
    nameScore = sum([ ord(char) - ord('A') + 1 \
                      for char in names[nameIdx] ])
    totalNameScores += namePosition * nameScore
  return totalNameScores

def main():
  start = clock()
  print SolveViaBruteForce(GetSortedNames(NAMES_FILENAME))
  print 'cputime = ' + str( clock() - start ) + ' sec'

if __name__ == '__main__':
  main()