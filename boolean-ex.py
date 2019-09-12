# A boolean is also an int . The bool type is a subclass of the int type and True and
# False are its only instances

issubclass(bool, int)  # True
isinstance(True, bool)  # True
isinstance(False, bool)  # True

print(isinstance(False, bool))
