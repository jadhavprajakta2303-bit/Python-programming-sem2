#program to find leap year
"""
Created on Tue Feb 10 12:44:27 2026

@author: Prajakta jadhav
"""
year=int(input("Enter year:"))
if(year%400==0) or (year%4==0 and year%100!=0):
   print("Leap year")
else:
     print("Not a leap year")
     


