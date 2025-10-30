calibration = 0

with open("Data/calibrations.txt") as f:
    for line in f.readlines():
        numbers = [int(x) for x in line if x.isdigit()]
        if len(numbers) > 0:
            calibration += numbers[0] * 10 + numbers[-1]

print(f"Total calibration: {calibration}")
