# lists

# The list type is probably the most commonly used collection type in Python. Despite its name, a list is more like an
# array in other languages, mostly JavaScript. In Python, a list is merely an ordered collection of valid Python values. A
# list can be created by enclosing values, separated by commas, in square brackets


int_list = [1, 2, 3]
string_list = ['abc', 'defghi']
mixed_list = [1, 'abc', True, 2.34, None]
nested_list = [['a', 'b', 'c'], [1, 2, 3]]
names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
print(names[0]) # Alice
print(names[2]) # Craig 
print(names[-1]) # Eric
print(names[-4]) # Bob

# Lists are mutable, so you can change the values in a list:

names[0] = 'Ann'
print(names)
names.append("Sia")
print(names)
names.insert(1, "Nikki")
print(names)

names.remove("Bob")
print(names) # Outputs ['Alice', 'Nikki', 'Craig', 'Diana', 'Eric', 'Sia']
names.index("Alice")

len(names)

a = [1, 1, 1, 2, 3, 4]
a.count(1)