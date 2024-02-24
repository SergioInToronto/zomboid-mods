#! /usr/bin/python3

import os


BASE_DIR = 'steamapps/workshop/content/108600/'


for folder in os.listdir(BASE_DIR):
    mod_path = os.path.join(BASE_DIR, folder, 'mods')
    subfolders = os.listdir(mod_path)

    # Some mods include... multiple mods. Often an "old" and latest version
    for mod_folder in subfolders:
        mod_info_path = os.path.join(mod_path, mod_folder, 'mod.info')

        with open(mod_info_path) as f:
            id_line = next(l for l in f if l.startswith("id="))
        mod_id = id_line.lstrip("id=").rstrip("\n")

        multiple = len(subfolders) > 1
        extra = multiple and "  !!!!! Multiple Mods !!!!!" or ""
        print(f"{mod_id}: {mod_folder} {extra}")
