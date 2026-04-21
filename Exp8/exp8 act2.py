# Handle invalid age input in registration form.
"""
Created on Tue Apr 21 07:53:09 2026

@author: Prajakta Jadhav
"""
try:
    age = int(input("Enter your age: "))

    if age < 0 or age > 120:
        raise ValueError("Invalid age entered!")

    print("Registration successful")

except ValueError as e:
    print("Error:", e)
