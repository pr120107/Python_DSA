"""
Puzzle 40 | (Find missing Row in Excel)

We are given an excel sheet which contains integers from 1 to 50, including both. However, the numbers are in a 
jumbled form and there is 1 integer missing. You have to write a code to identify the missing integer.
"""
n = 50
arr = []
for i in range (1, n + 1):
    if i != 25:
        pass
        arr.append(i)
print(arr)

expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)

missing_number = expected_sum - actual_sum
print(f"The missing number is: {missing_number}")