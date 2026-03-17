# Count frequency of items purchased
"""
Created on- Tue Mar 17 13:14:58 2026

@author: prajakta jadhav
"""

items = ["apple", "banana", "apple", "orange", "banana", "apple"]

frequency = {}

for item in items:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)
