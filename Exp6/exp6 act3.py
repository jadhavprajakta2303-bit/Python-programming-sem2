# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:55:34 2026

@author: Prajakta
"""
# Read and display all complaints from a file

filename = input("Enter complaint file name: ")

try:
    with open(filename, "r") as file:
        print("\n--- All Complaints ---")
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found. Please check the file name.")
except Exception as e:
    print("Error:", e)

