squares = [x * x for x in (1, 2, 3, 4)]
print(squares)

upper = [s.upper() for s in "Hello World"]
print(upper)

# Strip off any commas from the end of strings in a list
strippedData = [w.strip(',') for w in ['these,', 'words,,', 'mostly', 'have,commas,']]
print(strippedData)

sentence = "Beautiful is better than ugly"

# Organize letters in words more reasonably - in an alphabetical order
arrangedLetter = ["".join(sorted(word, key = lambda x: x.lower())) for word in sentence.split()]
print(arrangedLetter)

expr = [x if x in 'aeiou' else '*' for x in 'apple']
print(expr)

condionalList1 = [x for x in range(10) if x % 2 == 0]
print(condionalList1)

condionalList2 = [x if x % 2 == 0 else None for x in range(10)]
print(condionalList2)


list_1 = [1, 2, 3 , 4]
list_2 = ['a', 'b', 'c', 'd']
list_3 = ['6', '7', '8', '9']
combined1 = [(i,j,k) for i, j, k  in zip(list_1, list_2, list_3)]
print(combined1)
