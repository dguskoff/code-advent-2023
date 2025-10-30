import re
import time

seeds = []
seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []


def create_maps(
    seeds,
    seed_to_soil_map,
    soil_to_fertilizer_map,
    fertilizer_to_water_map,
    water_to_light_map,
    light_to_temperature_map,
    temperature_to_humidity_map,
    humidity_to_location_map,
    f,
):
    seed_line = f.readline().split(":")
    seeds.append([int(n) for n in re.split("\s+", seed_line[1].strip())])
    line = f.readline()
    line = f.readline()
    while line != "\n":
        line = f.readline()
        if line != "\n":
            seed_to_soil_map.append([int(n) for n in re.split("\s+", line.strip())])

    line = f.readline()
    while line != "\n":
        line = f.readline()
        if line != "\n":
            soil_to_fertilizer_map.append(
                [int(n) for n in re.split("\s+", line.strip())]
            )

    line = f.readline()
    while line != "\n":
        line = f.readline()
        if line != "\n":
            fertilizer_to_water_map.append(
                [int(n) for n in re.split("\s+", line.strip())]
            )

    line = f.readline()
    while line != "\n":
        line = f.readline()
        if line != "\n":
            water_to_light_map.append([int(n) for n in re.split("\s+", line.strip())])

    line = f.readline()
    while line != "\n":
        line = f.readline()
        if line != "\n":
            light_to_temperature_map.append(
                [int(n) for n in re.split("\s+", line.strip())]
            )

    line = f.readline()
    while line != "\n":
        line = f.readline()
        if line != "\n":
            temperature_to_humidity_map.append(
                [int(n) for n in re.split("\s+", line.strip())]
            )

    line = f.readline()
    while line != "\n" and line != "":
        line = f.readline()
        if line != "\n" and line != "":
            humidity_to_location_map.append(
                [int(n) for n in re.split("\s+", line.strip())]
            )


def get_destination_number(map, source):
    for d, s, r in map:
        if source in range(s, s + r):
            return d + source - s
    return source


with open("Data/_5_1.txt") as f:
    create_maps(
        seeds,
        seed_to_soil_map,
        soil_to_fertilizer_map,
        fertilizer_to_water_map,
        water_to_light_map,
        light_to_temperature_map,
        temperature_to_humidity_map,
        humidity_to_location_map,
        f,
    )

    soils = [get_destination_number(seed_to_soil_map, seed) for seed in seeds[0]]
    fertilizers = [
        get_destination_number(soil_to_fertilizer_map, soil) for soil in soils
    ]
    waters = [
        get_destination_number(fertilizer_to_water_map, fertilizer)
        for fertilizer in fertilizers
    ]
    lights = [get_destination_number(water_to_light_map, water) for water in waters]
    temperatures = [
        get_destination_number(light_to_temperature_map, light) for light in lights
    ]
    humidities = [
        get_destination_number(temperature_to_humidity_map, temperature)
        for temperature in temperatures
    ]
    locations = [
        get_destination_number(humidity_to_location_map, humidity)
        for humidity in humidities
    ]

    lowest_location = sorted(locations)[0]

    print(f"Lowest Location: {lowest_location}")
