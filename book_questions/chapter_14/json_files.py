import json

string_of_data = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ":null}'
# convert json content into python data
json_as_python_value = json.loads(string_of_data)
print(json_as_python_value)

python_value = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}
# convert python data into json
string_of_json_data = json.dumps(python_value)
print(string_of_json_data)