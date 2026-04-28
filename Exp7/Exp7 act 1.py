#Create a BankAccount class for deposit and withdrawal.
"""
Created on Tue Apr 28 13:12:09 2026

@author: Prajakta
"""
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Amount must be positive")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Amount must be positive")
    
    def get_balance(self):
        return self.balance

# Example
acc = BankAccount("Riya", 1000)
acc.deposit(500)
acc.withdraw(200)
