# Use math module to calculate EMI interest.
"""
Created on Tue Apr 28 13:27:22 2026

@author: Prajakta
"""

import math

# User input
p = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (in %): "))
t = float(input("Enter time (in years): "))

# Convert annual rate to monthly and time to months
monthly_rate = r / (12 * 100)
months = t * 12

# EMI calculation formula
emi = p * monthly_rate * math.pow(1 + monthly_rate, months) / (math.pow(1 + monthly_rate, months) - 1)

# Total payment and interest
total_payment = emi * months
total_interest = total_payment - p

print("Monthly EMI:", round(emi, 2))
print("Total Interest:", round(total_interest, 2))
print("Total Payment:", round(total_payment, 2))