def get_dimensions(record):
    return tuple([int(x) for x in record.split("x")])


def get_cubicle(dimensions):
    return dimensions[0] * dimensions[1] * dimensions[2]


ribbon_length_needed = 0

with open("Data/boxes.txt") as f:
    for line in f.readlines():
        (l, w, h) = get_dimensions(line)

        dimensions = [l, w, h]
        dimensions.sort()

        smallest_perimeter = dimensions[0] * 2 + dimensions[1] * 2

        ribbon_length_needed += smallest_perimeter + get_cubicle(dimensions)

print(f"Ribbon length needed: {ribbon_length_needed}")
