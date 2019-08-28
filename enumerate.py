for index, item in enumerate(['one', 'two', 'three', 'four']):
    print(index, '::', item)

x = map(lambda e: e.upper(), ['one', 'two', 'three', 'four'])
print(x)
