from json import load

with open("values.json", 'r+') as file:
    data = load(file)

print(data)