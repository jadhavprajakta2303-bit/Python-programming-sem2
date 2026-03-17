# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:41:41 2026

@author: prajakta jadhav
"""

# Number of items
items = int(input("Enter number of items: "))

# Number of copies (receipts)
copies = int(input("Enter number of copies: "))

for i in range(1, copies + 1):   # Outer loop for copies
    print("\nReceipt Copy:", i)
    
    for j in range(1, items + 1):   # Inner loop for items
        print("Item Number:", j)