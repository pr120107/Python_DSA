"""
Puzzle | Find the Initial Money

Rama started on a quest of visiting temples, with few coins in his pockets.

As soon as he visits any temple, the money in his pocket gets doubled and on 
his way out, he donates Rs. 100 to each temple. He visits 4 temples on his quest. 
After visiting the last temple, his pocket is empty of all the money, so how much 
money he had initially?
"""
money_after_last_temple = 0
donation_per_temple = 100
number_of_temples = 4

current_money = money_after_last_temple

for _ in range(number_of_temples):
    current_money += donation_per_temple
    current_money /= 2

print(f"The initial amount of money Rama had is: Rs. {current_money}")