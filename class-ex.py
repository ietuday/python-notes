class Person(object):
    """A simple class"""
    species = "Homo Spanies"

    def __init__(self, name):       # Special Method
        """This is the initializer. It's a special
            method (see below).
        """
        self.name = name

    def __str__(self):              # Special method
        """This method is run when Python tries
            to cast the object to a string. Return
            this string when using print(), etc.
        """
        return self.name

        """Reassign and print the name attribute."""
        self.name = renamed
        print("Now my name is {0}".format(self.name))


# 1 The class is made up of attributes (data) and methods (functions).

# 2 Attributes and methods are simply defined as normal variables and functions.

# 3 As noted in the corresponding docstring, the __init__() method is called the initializer. It's equivalent to the
# constructor in other object oriented languages, and is the method that is first run when you create a new
# object, or new instance of the class.

# 4 Attributes that apply to the whole class are defined first, and are called class attributes.

# 5 Attributes that apply to a specific instance of a class (an object) are called instance attributes. They are
# generally defined inside __init__(); this is not necessary, but it is recommended (since attributes defined
# outside of __init__() run the risk of being accessed before they are defined).

# 6 Every method, included in the class definition passes the object in question as its first parameter. The word
# self is used for this parameter (usage of self is actually by convention, as the word self has no inherent
# meaning in Python, but this is one of Python's most respected conventions, and you should always follow it)

# 7 Those used to object-oriented programming in other languages may be surprised by a few things. One is that
# Python has no real concept of private elements, so everything, by default, imitates the behavior of the
# C++/Java public keyword. For more information, see the "Private Class Members" example on this page

# 8 Some of the class's methods have the following form: __functionname__(self, other_stuff). All such
# methods are called "magic methods" and are an important part of classes in Python. For instance, operator
# overloading in Python is implemented with magic methods
# Instances
kelly = Person("Kelly")
joseph = Person("Joseph")
john_doe = Person("John Doe")

# Attributes
print(kelly.species)
print(joseph.species)
print(john_doe.species)
print(kelly.name)
print(joseph.name)
print(john_doe.name)

# Methods
print(kelly.__str__())
print(joseph.__str__())
print(john_doe.__str__())
print(john_doe.rename("John"))


# Python has class methods and static methods – special kinds of methods. Class methods work the same
# way as regular methods, except that when invoked on an object they bind to the class of the object instead of to the
# object. Thus m.__self__ = type(a). When you call such bound method, it passes the class of a as the first
# argument. Static methods are even simpler: they don't bind anything at all, and simply return the underlying
# function without any transformations


class D(object):
    multiplier = 2
    @classmethod
    def f(cls, x):
        return cls.multiplier * x

    @staticmethod
    def g(name):
        print("Hello, %s" % name)


D.f
# <bound method type.f of <class '__main__.D'>>
D.f(12)
# 24
D.g
# <function D.g at ...>
D.g("world")
# Hello, world


# class Country(object):
#     def __init__(self):
#         self.cities = []

#     def addCity(self, addCity):
#         self.cities.append(city)


# class City(object):
#     def __init__(self, numPeople):
#         self.people = []
#         self.numPeople = numPeople

#     def addPerson(self, person):
#         self.people.append(person)

#     def join_country(self, country):
#         self.country = country
#         country.addCity(self)

#         for i in range(self.numPeople):
#             person(i).join_city(self)


# class Person(object):
#     def __init__(self, ID):
#         self.ID = ID

#     def join_city(self, city):
#         self.city = city
#         city.addPerson(self)

#     def people_in_my_country(self):
#         x = sum([len(c.people) for c in self.city.country.cities])
#         return x

print([m for m in dir(list) if not m.startswith('__')])

# Output
# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
