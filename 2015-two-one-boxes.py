def get_dimensions(record):
    return tuple([int(x) for x in record.split("x")])


box_area = 0
additional_area = 0
paper_area_needed = 0
with open("Data/boxes.txt") as f:
    for line in f.readlines():
        (l, w, h) = get_dimensions(line)

        box_area = 2 * l * w + 2 * w * h + 2 * h * l

        dimensions = [l, w, h]
        dimensions.sort()

        additional_area = dimensions[0] * dimensions[1]

        paper_area_needed += box_area + additional_area

print(f"Paper area needed: {paper_area_needed}")
