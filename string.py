foo = 1
bar = 'bar'
baz = 3.14

print('{}, {} and {}'.format(foo, bar, baz))

print("X value is: {x_val}. Y value is: {y_val}.".format(x_val=2, y_val=3))

data = {'first': 'Hodor', 'last': 'Hodor!'}
print('{first} {last}'.format(**data))
print('{first} {last}'.format_map(data))

person = {'first': 'Arthur', 'last': 'Dent'}

print('{p[first]} {p[last]}'.format(p=person))


class Person(object):
 first = 'Zaphod'
 last = 'Beeblebrox'
print('{p.first} {p.last}'.format(p=Person()))

reverseHello = [char for char in reversed('hello')]
print(reverseHello)

newSentance = "Make sure to foo your sentence.".replace('foo', 'spam')
print(newSentance)

