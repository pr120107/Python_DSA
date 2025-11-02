people = {'A' : 1, 'B' : 2, 'C' : 5, 'D' : 8}
time_limit = 15

left = ['A', 'B', 'C', 'D']
right = []
total_time = 0

right.append('A')
right.append('B')
left.remove('A')
left.remove('B')
total_time+=people['B']
print("Left side", left, "Right side", right, "time taken", total_time, "minutes")

left.append('A')
right.remove('A')
total_time+=people['A']
print("Left side", left, "Right side", right, "time taken", total_time, "minutes")

left.remove('C')
left.remove('D')
total_time+=people['D']
right.append('C')
right.append('D')
print("Left side", left, "Right side", right, "time taken", total_time, "minutes")

right.remove('B')
left.append('B')
total_time+=people['B']
print("Left side", left, "Right side", right, "time taken", total_time, "minutes")

right.append('A')
right.append('B')
left.remove('A')
left.remove('B')
total_time+=people['B']
print("Left side", left, "Right side", right, "time taken", total_time, "minutes")

if (total_time <= time_limit):
    print("All crossed bridge in", total_time, "minutes.")
else:
    print("Cannot be crossed in", time_limit, "took", total_time, "to cross the bridge.")