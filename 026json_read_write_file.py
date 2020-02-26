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

# here we create new data_file.json file with write mode using file i/o operation
with open('./json_file2.json', "w") as file_write:
    # write json data into file
    json.dump(person_data, file_write)

with open('./json_file.json') as file_object:
    # store file data in object
    data = json.load(file_object)
    print(data)
