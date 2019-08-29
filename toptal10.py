# Write a function that prints the least integer that is not present in a given list and cannot be represented by the summation of the sub-elements of the list.

# E.g. For a = [1,2,5,7] the least integer not represented by the list or a slice of the list is 4, and if a = [1,2,2,5,7] then the least non-representable integer is 18.

import  itertools
sum_list = []
stuff = [1,2, 5, 7]
for L in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, L):
        sum_list.append(sum(subset))

new_list = list(set(sum_list))
new_list.sort()
for each in range(0,new_list[-1]+2):
    if each not in new_list:
        print(each)
        break