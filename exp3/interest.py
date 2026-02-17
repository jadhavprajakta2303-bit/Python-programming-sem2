#write python program to compute simple interest
"""
Created on Tue Feb 17 12:30:46 2026

@author:prajakta
"""
def simple_interest(principal,rate,time):
    si = (principal*rate*time)/100
    return si
#Taking input from the user
p=float(input("Enter principal amount:"))
r=float(input("Enter rate of interest:"))
t=float(input("Enter time(in years):"))
#funtion call 
interest=simple_interest(p,r,t)
print("simple interest is:",interest)
    
