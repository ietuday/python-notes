a = reversed('hello')
print(a)

# tuple : An ordered collection of n values of any type ( n >= 0 ).
a = (1, 2, 3)
print(a)

b = ('a', 1, 'python', (1, 2))
print(b)

b[2] = 'something else' # returns a TypeError

# Supports indexing; immutable; hashable if all its members are hashable

# list : An ordered collection of n values ( n >= 0 )
a = [1, 2, 3]
b = ['a', 1, 'python', (1, 2), [1, 2]]
b[2] = 'something else' # allowed

# Not hashable; mutable.

# set : An unordered collection of unique values. Items must be hashable.

a = {1, 2, 'a'}
print(a)


# dict : An unordered collection of unique key-value pairs; keys must be hashable.
a = {1: 'one',2: 'two'}
b = {'a': [1, 2, 3],'b': 'a string'}
print(a)
print(b)

# An object is hashable if it has a hash value which never changes during its lifetime (it needs a __hash__()
# method), and can be compared to other objects (it needs an __eq__() method). Hashable objects which
# compare equality must have the same hash value.

