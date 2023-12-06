#!/usr/bin/python3
""" script that adds all arguments to a Python list,
    and then save them to a file
"""
import sys
from pathlib import Path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    filename = "add_item.json"
    if not Path(filename).exists():
        with open(filename, "w") as fname:
            fname.write("[]")
    else:
        my_list = load_from_json_file(filename)
        my_list.extend(sys.argv[1:])
        save_to_json_file(my_list, filename)
