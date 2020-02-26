"""
Complex Object encoding use JSONEncoder
1. python object serialize to JSON string
2. JSON string deserialize to python object
"""

import json

# custom JSON encoding by using JSONEncoder
class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):    #if we encounter a complex object
            return (z.real, z.imag)
        else:
            return super().default(z)

def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct

# serialize a complex obj to JSON string
json_string = json.dumps(2 + 5j, cls=ComplexEncoder)
print(json_string)

# deserialize JSON string to complex obj
file_path = './027example_data_00.json'
with open(file_path) as complex_data:
    data = complex_data.read()
    z = json.loads(data, object_hook=decode_complex)
print(z)
