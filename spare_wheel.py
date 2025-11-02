tyre_life_km = 20000  # Each tyre has 20,000 km life
num_tyres = 5         # 1 spare and other 4 already on the car
max_distance = (tyre_life_km * num_tyres) // 4 # Divide total tyre life by 4 tyres in use at a time because only 4 tyres can be used simultaneously
print(f"Maximum distance the car can travel: {max_distance} km")