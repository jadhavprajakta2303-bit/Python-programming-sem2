# ATM withdrawal system handles insufficient balance.
"""
Created on Tue Apr 21 07:52:18 2026

@author: Prajakta Jadhav
"""

balance = 5000

try:
    amount = float(input("Enter withdrawal amount: "))
    
    if amount > balance:
        raise ValueError("Insufficient balance!")
    elif amount <= 0:
        raise ValueError("Enter valid amount!")
    else:
        balance -= amount
        print("Withdrawal successful!")
        print("Remaining balance:", balance)

except ValueError as e:
    print("Error:", e)

