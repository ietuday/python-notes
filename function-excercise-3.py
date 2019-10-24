# MAKES TWENTY:
# Given two integers, return True if the sum of the integers is 20
# *or* if one of the integers is 20. If not, return False


def makes_twenty(n1, n2):
    return (n1+n2) == 20 or n1 == 20 or n2 == 20


test1 = makes_twenty(10, 10)
test2 = makes_twenty(20, 10)
test3 = makes_twenty(10, 20)
test4 = makes_twenty(15, 19)

print(test1)
print(test2)
print(test3)
print(test4)
