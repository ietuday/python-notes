a = [1, 2, 3, 4]

for i in a:
    print(type(i))
    if type(i) is not int:
        print(i)
    break
else:
    print("no exception")
