# A set is a collection of elements with no repeats and without insertion order but sorted order. They are used in
# situations where it is only important that some things are grouped together, and not what order they were
# included. For large groups of data, it is much faster to check whether or not an element is in a set than it is to do
# the same for a list .

first_names = {'Adam', 'Beth', 'Charlie'}

#you can build a set using an existing list :

my_list = [1,2,3]
my_set = set(my_list)

if 4 in my_set:
    print('yes')
else:
    print('No')
