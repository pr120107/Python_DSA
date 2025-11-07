from itertools import product

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
genders = ['B', 'G']

outcomes = list(product(genders, days, repeat=2))  # 196 total

favorable_outcomes = []
both_boys_outcomes = []

for outcome in outcomes:
    first_child_is_boy_tue = (outcome[0] == 'B' and outcome[1] == 'Tue')
    second_child_is_boy_tue = (outcome[2] == 'B' and outcome[3] == 'Tue')

    if first_child_is_boy_tue or second_child_is_boy_tue:
        favorable_outcomes.append(outcome)

        if outcome[0] == 'B' and outcome[2] == 'B':
            both_boys_outcomes.append(outcome)

probability = len(both_boys_outcomes) / len(favorable_outcomes)
print(f"The probability that both children are boys given that at least one is a boy born on a Tuesday is: {probability:.4f}")


"""
Puzzle | Tuesday Boy Paradox

Ankur's elder brother got married 10 years ago. This summer, Ankur is going to meet his brother after a decade. As a token of love, he plans to buy clothes 
for his brother's kids.

From what is remembered, Ankur's brother has two children, and it is known that:

One of the children is a boy, and that boy was born on a Tuesday.
Assume:

Each child is equally likely to be a boy (B) or a girl (G).
Each child is equally likely to be born on any of the 7 days of the week, independent of sex.
What is the probability that both of Ankur's brother's children are boys, given that at least one of them is a boy born on a Tuesday?
"""

from itertools import product
def calculate_probability():
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    outcomes = list(product(['B', 'G'], days, repeat=2))
    favorable_outcomes = [
        outcome for outcome in outcomes
        if (outcome[0] == 'B' and outcome[1] == 'Tue') or (outcome[2] == 'B' and outcome[3] == 'Tue') 
    ]
    print("Number of favorable outcomes:", len(favorable_outcomes), "Which are:", favorable_outcomes)
    
    both_boys_outcomes = [
        outcome for outcome in favorable_outcomes
        if outcome[0] == 'B' and outcome[2] == 'B'
    ]
    print("Number of final favorable outcomes:", len(both_boys_outcomes), "Which are:", both_boys_outcomes)
    probability = len(both_boys_outcomes) / len(favorable_outcomes)
    return probability
if __name__ == "__main__":
    prob = calculate_probability()
    print(f"The probability that both children are boys given that at least one is a boy born on a Tuesday is: {prob:.4f}")


# Explanation:
# Total possible outcomes for two children = 2 (B/G) * 7 (days) * 2 (B/G) * 7 (days) = 196 because each child can be either a boy or a girl, 
# and can be born on any of the 7 days of the week.
# Outcomes with at least one boy born on Tuesday = 27
# Outcomes with both boys given at least one boy born on Tuesday = 13
# Probability = 13 / 27 ≈ 0.4815