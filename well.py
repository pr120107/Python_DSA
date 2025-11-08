well_depth = 50
climb_per_day = 4
slip_per_night = 3  
effective_climb_per_day = climb_per_day - slip_per_night
days = 0
current_height = 0
while True:
    days += 1
    current_height += climb_per_day
    if current_height >= well_depth:
        break
    current_height -= slip_per_night
print(f"The man will take {days} days to come out of the well.")

