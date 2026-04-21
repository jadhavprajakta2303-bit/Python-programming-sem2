#Prevent crash when dividing bill among zero people.
"""
Created on Tue Apr 21 07:55:32 2026

@author: prajakta Jadhav
"""
try:
    total_bill = float(input("Enter total bill amount: "))
    people = int(input("Enter number of people: "))

    amount_per_person = total_bill / people
    print("Each person should pay:", amount_per_person)

except ZeroDivisionError:
    print("Error: Number of people cannot be zero.")

except ValueError:
    print("Error: Please enter valid numeric values.")
