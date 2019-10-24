# OLD MACDONALD:
# Write a function that capitalizes the first and fourth letters of a name


def old_macdonald(name):
    if len(name) > 3:
        print(name[:3].capitalize())
        print(name[3:].capitalize())
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short'


test = old_macdonald('macdonald')
print(test)
