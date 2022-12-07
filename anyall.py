
a = [False, True, False, False]

print(any(a))
print(all(a))

people = ["Eric", "Beatrice", "Marie", "Paul", "Barbara", "Marie"]

for nom in people:
    found = False
    if "c" in nom.lower():
        found = True
        break
        
if found:
    print("Found")
else:
    print("Not Found")

print()

test = [True if "c" in nom.lower() else False for nom in people]
print(test)
result = any(test)
print(result)
if result:
    print("Trouve")
else:
    print("Non Trouve")

people = ["Eric", "Beatrice", "Marie", "Paul", "Barbara", "Marie"]

total = sum([len(nom) for nom in people])
print(total)
# somme = sum(total)
# print(somme)