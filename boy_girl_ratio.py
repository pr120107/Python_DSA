"""
Puzzle | The Boy Preference Ratio Riddle

In a country, every family continues to have children until they have a boy, 
after which they stop having more children. Assuming the probability of having 
a boy or a girl is equal (50%), what is the expected ratio of boys to girls in 
the overall population?
"""
# Simulate the process to estimate the ratio

def simulate_births(num_families):
    total_boys = 0
    total_girls = 0
    
    for _ in range(num_families):
        boys = 0
        girls = 0
        while boys == 0:  # Continue until a boy is born
            if random.choice([0, 1]) == 1:
                boys += 1
            else:
                girls += 1
        
        total_boys += boys
        total_girls += girls
    return total_boys, total_girls
import random
if __name__ == "__main__":
    num_families = 100000
    total_boys, total_girls = simulate_births(num_families)
    ratio = total_boys / total_girls if total_girls > 0 else float('inf')
    
    print(f"Total Boys: {total_boys}")
    print(f"Total Girls: {total_girls}")
    print(f"Boy to Girl Ratio: {ratio:.4f}")