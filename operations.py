

noms = ["Jean", "Sophie", "Christophe", "Zoe", "Pierre"] 

ages = [3, 16, 43, 20, 22]
print(min(ages)) #3
print(min(noms)) # Christophe premiere lettre est minimale par ordre alpha

if "Jean" in noms:
    print("present")
else:
    print("absent")

print(sum(ages))

#swapping
print(noms)
noms[0], noms[4] = noms[4], noms[0] # valable pour x items
print(noms)

#join split
print("Join...")
nom_join = ", ".join(noms)
nom_rebuild = nom_join.split(", ")
print(nom_join)

print("Rebuided")
print(nom_rebuild)
a = "Paul, Pierre, Jean, Mathieu"
b = "Paul-Pierre-Jean-Mathieu"

a_split = a.split(", ")
b_split = b.split("-")
print(a_split)
print(b_split)

#index, find & count

noms = ["Jean", "Sophie", "Pierre", "Christophe", "Pierre", "Zoe", "Pierre"] 
#find index from name
name = "Pierre"
nb_occur = noms.count(name)
print("occurences", nb_occur)
# if name in noms:
if nb_occur > 0:
    index_occur = 0
    #print(noms.index(name))
    print("index...")
    print(noms.index(name, 3)) # preciser start index - 3
    # boucler is plusieurs index
    for i in range(nb_occur):
        index_occur = noms.index(name, index_occur)
        print(name, "trouve a", index_occur)
        index_occur += 1
        


else:
    print("element not in the collection")


# si plusieurs memes elements


chaine = "Marie Bedia Cenatus"

f = chaine.find("BEdia") # si trouver return index sinon return -1 
print(f)













