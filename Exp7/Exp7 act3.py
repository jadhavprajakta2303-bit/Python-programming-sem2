# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:20:24 2026

@author: Prajakta 
"""

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self, bonus):
        total = self.base_salary + bonus
        print(f"Employee: {self.name} | Total Salary: ${total}")
        return total

# Example usage:
emp = Employee("John", 5000)
emp.calculate_salary(500)