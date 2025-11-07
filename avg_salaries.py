"""
Puzzle | Know Average Salary without Disclosing Salaries

Three Employees want to know the average of their salaries. They are not allowed to share their individual salaries.
Interview question - Bloomberg user defined inputs to be taken for dummy  values
"""

salary1 = int(input("Enter salary of Employee 1: "))
salary2 = int(input("Enter salary of Employee 2: "))
salary3 = int(input("Enter salary of Employee 3: "))
average = (salary1 + salary2 + salary3) / 3
print(f"The average salary is: {average:.2f}")