
#  Lambda Function

# An anonymous, inlined function defined with lambda. The parameters of the lambda are defined to the left of the
# colon. The function body is defined to the right of the colon. The result of running the function body is (implicitly)
# returned.

# s=lambda x:x*x
# s(2) =>4

def greet_me(): return "Hello"


def strip_and_upper_case(s): return s.strip().upper()


strip_and_upper_case(" Hello ")

greeting = lambda x, *args, **kwargs: print(x, args, kwargs)
greeting('hello', 'world', world='world')

sorted([" foo ", " bAR", "BaZ "], key=lambda s: s.strip().upper())
# Out:
# [' bAR', 'BaZ ', ' foo ']

sorted([" foo ", " bAR", "BaZ "], key=lambda s: s.strip())

sorted(map(lambda s: s.strip().upper(), [" foo ", " bAR", "BaZ "]))

sorted(map(lambda s: s.strip(), [" foo ", " bAR", "BaZ "]))

my_list = [3, -4, -2, 5, 1, 7]
sorted(my_list, key=lambda x: abs(x))
# [1, -2, 3, -4, 5, 7]

my_list = [3, -4, -2, 5, 1, 7]
sorted( my_list, key=lambda x: abs(x))
# [3, 5, 1, 7]

list( map( lambda x: abs(x), my_list))
# Out:
# [3, 4, 2, 5, 1, 7]



