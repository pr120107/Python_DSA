# Number of bottles and rats
num_bottles = 1000
num_rats = 10

# Let's assign each bottle a binary label
# 10 bits are enough because 2^10 = 1024 >= 1000
bottle_labels = [format(i, '010b') for i in range(num_bottles)]

# Let's randomly choose one poisoned bottle
import random
poisoned_bottle = random.randint(0, num_bottles - 1)
print(f"💀 The poisoned bottle is #{poisoned_bottle} (binary {bottle_labels[poisoned_bottle]})")

# Step 1: Assign samples to rats
# Each rat will drink from bottles where its bit = 1
rat_samples = {rat: [] for rat in range(num_rats)}
for i, label in enumerate(bottle_labels):
    for rat in range(num_rats):
        if label[num_rats - 1 - rat] == '1':  # bit position (reversed for clarity)
            rat_samples[rat].append(i)

# Step 2: Simulate the test results
rat_results = [0] * num_rats  # 0 = alive, 1 = dead
for rat in range(num_rats):
    if poisoned_bottle in rat_samples[rat]:
        rat_results[rat] = 1  # this rat drank poisoned wine

# Step 3: Decode which bottle was poisoned from the dead/alive pattern
# Convert the binary pattern of rat_results to a number
binary_pattern = ''.join(str(bit) for bit in reversed(rat_results))
decoded_bottle = int(binary_pattern, 2)

print("\n🐀 Rat Results (0=alive, 1=dead):", rat_results)
print(f"Binary pattern of deaths: {binary_pattern}")
print(f"💡 Decoded poisoned bottle number: {decoded_bottle}")
print(f"✅ Match? {decoded_bottle == poisoned_bottle}")