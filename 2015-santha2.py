floor = 0
position = 0
with open("Data/parantacies.txt") as f:
    for char in f.read():
        if char == "(":
            floor += 1
        else:
            floor -= 1
        position += 1

        if floor == -1:
            print(f"Position = {position}")
            break
