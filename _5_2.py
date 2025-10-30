import re
import numpy as np
from bisect import bisect_left
import time

seeds = []
seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []
b = 0


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
    global b
    b += 1
    if b == 1 or b % 50000000 == 0:
        print(b, source)
    for d, s, r in map:
        if source in range(s, s + r):
            return d + source - s
    return source


# def get_destination_number_1(map, source):


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

    seeds_start_and_range = np.array(seeds).reshape(-1, 2).tolist()
    all_locations = []
    i = 0
    for start, r in seeds_start_and_range:
        seeds_final = []
        a = time.time()
        seeds_final.extend([*range(start, start + r)])
        print(i, "start", len(seeds_final), time.time() - a)

        b = 0
        print("soil", len(seeds_final), time.time() - a)
        soils = [get_destination_number(seed_to_soil_map, seed) for seed in seeds_final]
        seeds_final.clear()

        b = 0
        print(i, "fertilizers", len(soils), time.time() - a)
        fertilizers = [
            get_destination_number(soil_to_fertilizer_map, soil) for soil in soils
        ]
        soils.clear()

        b = 0
        print(i, "water", time.time() - a)
        waters = [
            get_destination_number(fertilizer_to_water_map, fertilizer)
            for fertilizer in fertilizers
        ]
        fertilizers.clear()

        b = 0
        print(i, "light", time.time() - a)
        lights = [get_destination_number(water_to_light_map, water) for water in waters]
        waters.clear()

        b = 0
        print(i, "temp", time.time() - a)
        temperatures = [
            get_destination_number(light_to_temperature_map, light) for light in lights
        ]
        lights.clear()

        b = 0
        print(i, "humid", time.time() - a)
        humidities = [
            get_destination_number(temperature_to_humidity_map, temperature)
            for temperature in temperatures
        ]
        temperatures.clear()

        b = 0
        print(i, "locations", time.time() - a)
        locations = [
            get_destination_number(humidity_to_location_map, humidity)
            for humidity in humidities
        ]
        humidities.clear()

        all_locations.extend(locations)
        locations.clear()
        i = +1

    print("Sorting Locations...")
    lowest_location = sorted(all_locations)[0]
    print(f"Lowest Location: {lowest_location}")
