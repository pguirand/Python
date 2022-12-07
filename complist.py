people = ["Eric", "Marie", "Beatrice", "Marie", "Paul", "Barbara", "Marie"]

numbers = []
for item in people:
    numbers.append(len(item))

print(numbers)


test = ["hello "+item for item in people]
print(test)

liste = [len(item) for item in people if len(item)<5]
print(liste)

liste = [item for item in people if "e" in item]
print(liste)

liste = [item if len(item) < 6 else 0 for item in people]
print(liste)

a = [i for i in range(10) if (i//2)*2 == i]
print(a)

b = [(item, True if (item//2)*2 == item else False) for item in range(10)]
print(b)
