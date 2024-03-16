#! /usr/bin/python3

import json
import subprocess


# Run from server directory
MAPS_DIR = 'media/maps/'
IGNORE_MAPS = [
    # these are defaults, or otherwise unwanted maps
    "Muldraugh, KY",
    "West Point, KY",
    "Rosewood, KY",
    "Riverside, KY",
    "challengemaps/Kingsmouth",
    "challengemaps/Studio",
]

output = subprocess.check_output(['find', '-L', MAPS_DIR, '-type', 'f', '-name', 'spawnpoints.lua'])
file_paths = output.decode("utf-8").strip().split("\n")

for path in file_paths:
    map_name = path.removeprefix(MAPS_DIR).removesuffix('/spawnpoints.lua')
    if map_name in IGNORE_MAPS:
        continue
    print(f'{{ name = "{map_name}", file = "{path}"}},')
