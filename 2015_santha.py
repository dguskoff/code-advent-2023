floor = 0
with open("Data/parantacies.txt") as f:
    for char in f.read():
        if char == "(":
            floor += 1
        else:
            floor -= 1
print(f"Floors = {floor}")
