# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:47:46 2026

@author: prajakta jadhav
"""

# Generate multiplication tables from 1 to 10

for i in range(1, 11):   # Tables from 1 to 10
    print("\nTable of", i)
    
    for j in range(1, 11):   # Multiply from 1 to 10
        print(i, "x", j, "=", i * j)