# Filter takes a function and a collection. It returns a collection of every item for which the function returned True.

from itertools import filterfalse
arr = [1, 2, 3, 4, 5, 6]
res = [i for i in filter(lambda x:x > 4, arr)]
print(res)
# outputs[5,6]

names = ['Fred', 'Wilma', 'Barney']


def long_name(name):
    return len(name) > 5


result = list(filter(long_name, names))
print(result)


result = list(filter(None, [1, 0, 2, [], '', 'a']))

print(result)


result = list(filterfalse(None, [1, 0, 2, [], '', 'a']))
print(result)
