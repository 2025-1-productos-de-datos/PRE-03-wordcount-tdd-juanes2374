import os

def read_all_lines(input_folder):
    lines = []
    for filename in os.listdir(input_folder):
        filepath = os.path.join(input_folder, filename)
        if os.path.isfile(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                lines.extend(f.readlines())
    return lines
