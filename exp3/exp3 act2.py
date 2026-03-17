# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:44:43 2026

@author: prajakta jadhav
"""

# Function to calculate EMI
def calculate_emi(principal, rate, years):
    monthly_rate = rate / (12 * 100)   # Convert annual rate to monthly
    months = years * 12

    emi = (principal * monthly_rate * (1 + monthly_rate) * months) / ((1 + monthly_rate) * months - 1)
    return emi

# Taking input from user
p = float(input("Enter loan amount: "))
r = float(input("Enter annual interest rate (%): "))
y = int(input("Enter loan period (years): "))

# Function call
emi = calculate_emi(p, r, y)