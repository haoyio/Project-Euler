#!/usr/bin/env python

from time import clock
import calendar

START_YEAR = 1901
END_YEAR = 2000
START_MONTH = 1     # January
END_MONTH = 12      # December
SUNDAY_INDEX = 0
START_DAY = 2       # Tuesday
DAYS_IN_WEEK = 7

def SolveViaCalendar():
  years = range( START_YEAR, END_YEAR + 1 )
  months = range( START_MONTH, END_MONTH + 1 )
  nSundays = 0
  for year in years:
    for month in months:
      if calendar.SUNDAY == \
         calendar.monthrange( year, month )[ SUNDAY_INDEX ]:
        nSundays += 1
  return nSundays

def IsLeapYear( year ):
  return year % 4 == 0 and year % 400 != 0

def GetNumberOfDaysInMonth( month, year ):
  if month in [ 1, 3, 5, 7, 8, 10, 12 ]:
    return 31
  elif month in [ 4, 6, 9, 11 ]:
    return 30
  elif IsLeapYear( year ):
    return 29
  else:
    return 28

def SolveViaCounting():
  '''
  Count the number of Sundays via a brute force approach. Note
  the convention of having Sundays = 0 and so forth. 
  '''
  years = range( START_YEAR, END_YEAR + 1 )
  months = range( START_MONTH, END_MONTH + 1 )
  nSundays = 0
  day = START_DAY
  for year in years:
    for month in months:
      if day == SUNDAY_INDEX:
        nSundays += 1
      day = ( day + GetNumberOfDaysInMonth( month, year ) ) % DAYS_IN_WEEK
  return nSundays

def main():
  start = clock()
  # print SolveViaCalendar()
  print SolveViaCounting()
  print "cputime = " + str( clock() - start ) + " sec"

if __name__ == "__main__":
  main()