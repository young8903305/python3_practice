"""
Complex Object encoding use JSONEncoder
1. python object serialize to JSON string
2. JSON string deserialize to python object
"""

import json


class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)

def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct

json_string = json.dumps(2 + 5j, cls=ComplexEncoder)
print(json_string)

with open('027example_data.json') as complex_data:
    data = complex_data.read()
    z = json.loads(data, object_hook=decode_complex)
print(z)