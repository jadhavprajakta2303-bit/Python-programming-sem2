#python program using nested loop
"""
Created on Tue Feb 17 12:15:28 2026

@author:prajakta
"""
n=int(input("Enter number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()    
