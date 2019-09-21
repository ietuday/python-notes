# A dictionary in Python is a collection of key-value pairs. The dictionary is surrounded by curly braces. Each pair is
# separated by a comma and the key and value are separated by a colon. Here is an example

state_capitals = {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento',
    'Georgia': 'Atlanta'
}

# To get a value, refer to it by its key:

ca_capital = state_capitals['California']

for k in state_capitals.keys():
    print('{0} is the capital of {1}'.format(state_capitals[k], k))


# Dictionaries strongly resemble JSON syntax. The native json module in the Python standard library can be used to
# convert between JSON and dictionaries
d = {"a": 1, "b": 2, "c": 3}

for key, value in d.items():
    print(key, "::", value)

fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
fishdog = {**fish, **dog}
print(fishdog)

d = {'k1': 100, 'k2': 200, 'k3': 300}
print(d.keys())
print(d.values())
print(d.items())
