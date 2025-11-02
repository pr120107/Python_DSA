'''Puzzle | Poison and Rat

You have 1000 wine bottles. Exactly one bottle is poisoned.

A rat that drinks the poisoned wine will die within 1 hour.
(Assume rats can each sip any number of samples once at the start.)
Determine the minimum number of rats needed to identify which single bottle is poisoned in 1 hour.'''

# Krrish code 
# import math

# def min_rats_needed(num_bottles):
#     """
#     Calculate the minimum number of rats needed to identify the poisoned bottle.
#     Uses the concept that n rats can identify 2^n different bottles because each rat
#     represents one bit in a binary number (dead=1, alive=0).
    
#     Args:
#         num_bottles: Total number of wine bottles to test
    
#     Returns:
#         The minimum number of rats needed
#     """
#     return math.ceil(math.log2(num_bottles))

# def assign_bottles_to_rats(num_bottles, num_rats):
#     """
#     Create a testing strategy by assigning bottles to rats.
#     Each bottle's number (minus 1) is converted to binary, and each 1 in that binary
#     number means the corresponding rat should drink from that bottle.
    
#     For example, for bottle 5 (binary 0100 with 4 rats):
#         - Rat 1 (rightmost bit): doesn't drink (0)
#         - Rat 2: doesn't drink (0)
#         - Rat 3: drinks (1)
#         - Rat 4 (leftmost bit): doesn't drink (0)
    
#     Args:
#         num_bottles: Total number of bottles
#         num_rats: Number of rats available
    
#     Returns:
#         List where index i contains list of bottle numbers rat i should drink from
#     """
#     # Initialize empty lists for each rat
#     rat_assignments = [[] for _ in range(num_rats)]
    
#     # For each bottle (0 to num_bottles-1)
#     for bottle in range(num_bottles):
#         # Convert to binary with leading zeros
#         # e.g., for 4 rats: 5 becomes '0101'
#         binary = format(bottle, f'0{num_rats}b')
        
#         # Assign bottle to rats based on 1's in binary number
#         for rat in range(num_rats):
#             if binary[rat] == '1':
#                 # Add 1 to bottle number for 1-based indexing
#                 rat_assignments[rat].append(bottle + 1)
    
#     return rat_assignments

# def find_poisoned_bottle(dead_rats, num_rats):
#     """
#     Determine which bottle is poisoned based on which rats died.
#     The pattern of dead/alive rats forms a binary number where:
#         - dead rat = 1
#         - alive rat = 0
#     This binary number + 1 is the poisoned bottle number.
    
#     Args:
#         dead_rats: List of booleans where dead_rats[i] is True if rat i died
#         num_rats: Total number of rats used
    
#     Returns:
#         The number of the poisoned bottle (1-based indexing)
#     """
#     # Convert dead/alive pattern to binary string
#     binary = ''
#     for i in range(num_rats):
#         binary = ('1' if dead_rats[i] else '0') + binary
    
#     # Convert binary to decimal and add 1 for 1-based bottle numbering
#     return int(binary, 2) + 1

# def main():
#     # Test case with 1000 bottles
#     num_bottles = 1000
    
#     # Calculate minimum rats needed
#     num_rats = min_rats_needed(num_bottles)
#     print(f"For {num_bottles} bottles, we need {num_rats} rats")
    
#     # For demonstration, we'll assume bottle 123 is poisoned
#     poisoned_bottle = 123
#     print(f"\nLet's simulate with bottle {poisoned_bottle} being poisoned:")
    
#     # Get the testing strategy (which rats drink which bottles)
#     rat_assignments = assign_bottles_to_rats(num_bottles, num_rats)
    
#     # Simulate the experiment
#     # Initialize all rats as alive
#     dead_rats = [False] * num_rats
    
#     # Convert poisoned bottle number to binary to determine which rats die
#     # Subtract 1 because we used 1-based bottle numbering
#     poisoned_binary = format(poisoned_bottle - 1, f'0{num_rats}b')
    
#     # Mark rats as dead based on binary representation
#     for i in range(num_rats):
#         if poisoned_binary[i] == '1':
#             dead_rats[i] = True
    
#     # Display results of the experiment
#     print("\nRat status after 1 hour:")
#     for i in range(num_rats):
#         status = "Dead" if dead_rats[i] else "Alive"
#         print(f"Rat {i + 1}: {status}")
    
#     # Use the pattern of dead rats to identify the poisoned bottle
#     identified_bottle = find_poisoned_bottle(dead_rats, num_rats)
#     print(f"\nBased on which rats died, the poisoned bottle is: {identified_bottle}")

# if __name__ == "__main__":
#    main()