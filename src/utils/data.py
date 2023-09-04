import json

def write_file(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

