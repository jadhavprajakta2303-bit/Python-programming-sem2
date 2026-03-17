#Find students present in both classes
"""
Created on Tue Mar 17 13:04:42 2026

@author:prajakta jadhav
"""

classA = {1, 2, 3, 4, 5}
classB = {4, 5, 6, 7}

# Common students
common = classA.intersection(classB)

print(common)