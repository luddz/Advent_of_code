import os 

temp_cal = 0
cal_carried = []
with open("day-1-input.py", 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
        if line == "\n":
            cal_carried.append(temp_cal)
            temp_cal = 0
        else: 
            temp_cal += int(line)
    
    cal_carried.append(temp_cal)

cal_carried.sort()
print("----------------")
print(cal_carried[-3:])
print(f"{sum(cal_carried[-3:])=}")
