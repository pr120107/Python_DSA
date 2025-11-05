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