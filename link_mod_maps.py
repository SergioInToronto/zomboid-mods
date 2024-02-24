#! /usr/bin/python3

import os
import subprocess


BASE_DIR = '../../steamapps/workshop/content/108600/'
MAPS_DIR = '.'


output = subprocess.check_output(['find', BASE_DIR, '-type', 'd', '-name', 'maps'])
map_folders = output.decode("utf-8").strip().split("\n")
for folder in map_folders:
    maps = os.listdir(folder)
    for map_name in maps:
        map_path = os.path.join(folder, map_name)
        dest_dir = os.path.join(MAPS_DIR, map_name)
        if os.path.exists(dest_dir):
            continue
        subprocess.run(['ln', '-f', '-s', map_path, dest_dir], check=True)
