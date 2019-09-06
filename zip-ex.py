zip returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument
sequences or iterables

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
    print(a, b)

alist = ['a1', 'a2', 'a3']
blist = ['b1']
clist = ['c1', 'c2', 'c3', 'c4']
for a, b, c in itertools.zip_longest(alist, blist, clist):
    print(a, b, c)
