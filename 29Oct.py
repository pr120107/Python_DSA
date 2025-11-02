'''
There are 4 people (A, B, C, and D) who want to cross a bridge at night.

A, B, C and D take 1, 2, 5 and 8 minutes respectively to cross the bridge.
There is only one torch with them, and the bridge cannot be crossed without the torch.
There cannot be more than two people on the bridge at any time, and when two people cross the bridge together, they must move at the slower person's pace.
Can they all cross the bridge in 15 minutes?
'''
# 1-3: Define the function and initialize the crossing times and total time limit.
# 5-8: Set the initial state with all people on the left side of the bridge.
# 10-12: First crossing of A and B, updating the total time and sides.
# 14-16: A returns with the torch, updating the total time and sides.
# 18-20: C and D cross together, updating the total time and sides.
# 22-24: B returns with the torch, updating the total time and sides.
# 26-28: A and B cross again, updating the total time and sides.
# 30-34: Check if the total time is within the limit and return the result.
# 36-40: Call the function and print the result.
def bridge_crossing():
    # Time taken by each person to cross the bridge
    times = {'A': 1, 'B': 2, 'C': 5, 'D': 8}
    
    # Total time limit
    total_time_limit = 15
    
    # Initial state: all on the left side
    left_side = ['A', 'B', 'C', 'D']
    right_side = []
    total_time = 0
    
    # Strategy to minimize time
    # Step 1: A and B cross (2 minutes)
    right_side.extend(['A', 'B'])
    total_time += times['B']
    left_side.remove('A')
    left_side.remove('B')
    
    # Step 2: A returns (1 minute)
    left_side.append('A')
    total_time += times['A']
    right_side.remove('A')
    
    # Step 3: C and D cross (8 minutes)
    right_side.extend(['C', 'D'])
    total_time += times['D']
    left_side.remove('C')
    left_side.remove('D')
    
    # Step 4: B returns (2 minutes)
    left_side.append('B')
    total_time += times['B']
    right_side.remove('B')
    
    # Step 5: A and B cross again (2 minutes)
    right_side.extend(['A', 'B'])
    total_time += times['B']
    left_side.remove('A')
    left_side.remove('B')
    
    # Check if all have crossed within the time limit
    if total_time <= total_time_limit:
        return True, total_time
    else:
        return False, total_time
result, time_taken = bridge_crossing()
if result:
    print(f"All people crossed the bridge in {time_taken} minutes.")
else:
    print(f"Could not cross the bridge within the time limit. Time taken: {time_taken} minutes.")

# Explanation of code
# The code defines a function `bridge_crossing` that simulates the crossing of four people over a bridge with specific constraints.
# It calculates the total time taken for all four to cross using a strategy that minimizes the total crossing time.
# The function returns whether they can cross within the 15-minute limit and the total time taken.
# Line to line explanation with functions