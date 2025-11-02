total_rupees = 15
cost = 1
wrappers_for_a_chocolate = 3
chocolate_bought = total_rupees // cost
total_chocolates = chocolate_bought
wrappers = chocolate_bought
while wrappers >= wrappers_for_a_chocolate:
    additional_chocolates = wrappers // wrappers_for_a_chocolate
    print("Chocolates after exchange",additional_chocolates)
    total_chocolates += additional_chocolates
    wrappers = (wrappers % wrappers_for_a_chocolate) + additional_chocolates
    print("Wrappers of chocolate after every purchase:-",wrappers)
print(f"Maximum chocolates that can be eaten: {total_chocolates}")
print(5//3) #Floor function
print(5%3) #Gives remainder as output
#53=>1
#5%3=>2