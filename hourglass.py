hourglass_1 = 7
hourglass_2 = 4
wished_time = 9
passed_time = 0
hourglass_1_running = True
hourglass_2_running = True
while passed_time != wished_time:
    if hourglass_1_running:
       hourglass_1 -= 1
    if hourglass_2_running:
       hourglass_2 -= 1
    passed_time+=1
    if hourglass_1 == 0:
       hourglass_1 = 7
       hourglass_1_running = not hourglass_1_running
    if hourglass_2 == 0:
       hourglass_2 = 4
       hourglass_2_running = not hourglass_2_running
print("Total time passed is:", passed_time, "minutes and remaining time is:", (hourglass_1 + hourglass_2) - passed_time, "minutes.")