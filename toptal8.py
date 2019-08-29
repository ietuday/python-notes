Given the following subclass of dictionary:

class DefaultDict(dict):
  def __missing__(self, key):
    return []
Will the code below work? Why or why not?

d = DefaultDict()
d['florp'] = 127

# Actually, the code shown will work with the standard dictionary object in python 2 or 3—that is normal behavior. Subclassing dict is unnecessary. However, the subclass still won’t work with the code shown because __missing__ returns a value but does not change the dict itself:

# d = DefaultDict()
# print d
# {}
# print d['foo']
# []
# print d
# {}
# So it will “work,” in the sense that it won’t produce any error, but doesn’t do what it seems to be intended to do.

# Here is a __missing__-based method that will update the dictionary, as well as return a value:

# class DefaultDict(dict):
#     def __missing__(self, key):
#         newval = []
#         self[key] = newval
#         return newval
# But since version 2.5, a defaultdict object has been available in the collections module (in the standard library.)


