# Write a function takes a two-word string and returns True if both words begin with same letter


def animal_crackers(text):
    worldlist = text.split()
    print(worldlist)
    print(worldlist[0][0])
    print(worldlist[1][0])
    return worldlist[0][0] == worldlist[1][0]


test = animal_crackers('Levelheaded Llama')
test2 = animal_crackers('Crazy Kangaroo')

print(test)
print(test2)
