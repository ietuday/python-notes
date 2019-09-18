print("gg" in "eggs")

lists = [[]] * 3
print(lists)

lists[0].append(3)
print(lists)

# What has happened is that [[]] is a one-element list containing an empty list, so all three elements of [[]] * 3 are references to this single empty list. Modifying any of the elements of lists modifies this single list. You can create a list of different lists this way:
[[] for i in range(3)]
