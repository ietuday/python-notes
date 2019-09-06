a = 2
print(a)

b = 9223372036854775807

print(b)

pi = 3.14
print(pi)

c = 'A'
print(c)

name = 'John Doe'
print(name)

q = True
print(q)

x = None
print(x)

print(type(a))


# a, b, c = 1, 2
# print(a, b, c)

# dummy variable can have any name, but it is conventional to use the underscore ( _ ) for assigning unwanted
# values

a,b,_ = 1, 2, 3
print(a,b)

a, b, _ = 1, 2, 3
print(a, b)

# Note that the number of _ and number of remaining values must be equal. Otherwise 'too many values to unpack
# error' is thrown

a = b = c = 1
print(a, b, c)



b = 2
print(a, b,c)

x = y = [7,8,9]
x = [13,8,22]

print(x)
print(y)

x = y = [7, 8, 9]
8, 9]
x[0] = 13

print(y)

x = [1, 2, [3, 4, 5], 6, 7]
print(x[2])
print(x[2][1])