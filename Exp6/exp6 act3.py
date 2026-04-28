# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:21:34 2026

@author: Rutuja Gaikwad

"""
def simple_interest(principal, rate, time):
    si = (principal*rate*time)/100
    return si
#Taking input from the user
p = float(input("Enter principal amount:"))
r = float(input("Enter rate of interet:"))
t = float(input("Enter time(in years):"))
# Function call
interest = simple_interest(p,r,t)
print("Simple interest is:", interest)
    