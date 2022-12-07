
distance_totale = [1.6, 0.25, 0.4, 0.5, 2.2, 3.6, 7, 1.8]
chauffeurs = ["Pierre", "Gol", "Noe", "Maria", "Alain", "Chantale", "David", "Eric"]
distance_min = distance_totale[0]

for distance in distance_totale:
    if distance < distance_min:
        distance_min = distance

print("Distance Minimale : ", distance_min, "m")

distance_min = distance_totale[0]
index_min = 0

for i in range(len(distance_totale)):
    distance = distance_totale[i]
    if distance < distance_min:
        distance_min = distance
        index_min = i

print("Distance Minimale : ", distance_min, "m. Chauffeur :",chauffeurs[index_min])

# distance_totale.sort()
# print(distance_totale[0])

nom_dist = [("Pierre",1.6), ("Gol",0.25), ("Noe",0.4), ("Maria",0.5), ("Alain",0.2), ("Chantale",3.6), ("David",7), ("Eric",1.8)]
print(nom_dist)

nom_e_dist_min = nom_dist[0]
for name in nom_dist:
    if name[1] < nom_e_dist_min[1]:
        nom_e_dist_min = name
        
print(nom_e_dist_min)