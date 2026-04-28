# Create a Student class that calculates grade.
"""
Created on Tue Apr 28 13:16:32 2026

@author: Prajakta
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks # list of marks
    
    def calculate_grade(self):
        avg = sum(self.marks) / len(self.marks)
        if avg >= 90:
            grade = 'A'
        elif avg >= 75:
            grade = 'B'
        elif avg >= 60:
            grade = 'C'
        elif avg >= 40:
            grade = 'D'
        else:
            grade = 'F'
        return avg, grade
    
    def display_result(self):
        avg, grade = self.calculate_grade()
        print(f"{self.name} | Average: {avg:.2f} | Grade: {grade}")

# Example
s1 = Student("Neha", [85, 90, 78, 92])
s1.display_result()