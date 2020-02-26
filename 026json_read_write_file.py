import json

person_data = {
    "name": "Ken",
    "age": 45,
    "married": True,
    "children": ("Alice", "Bob"),
    "pets": ['Dog'],
    "cars": [
        {"model": "Audi A1", "mpg": 15.1},
        {"model": "Zeep Compass", "mpg": 18.1}
    ]
}

write_file_path = './026json_write_out.json'
# here we create new data_file.json file with write mode using file i/o operation
with open(write_file_path, "w") as file_write:
    # write json data into file
    json.dump(person_data, file_write)

read_file_path = './026json_read_in.json'
with open(read_file_path) as file_object:
    # store file data in object
    data = json.load(file_object)
    print(data)
