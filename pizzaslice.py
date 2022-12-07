
# def tri_person(e):
#     return len(e)

def ajouter_pizza(pizzas):
    p = input("Entrer nouvelle Pizza : ")
    # ou encore
    if p in pizzas:
    # if pizza_existe(pizzas, nouv_pizza):
        print("Pizza existe deja, Ajout annule ...")
        return
    else:
        pizzas.append(p)

def afficher(collection, first=-1):
    # collection.sort()
    # collection.sort(reverse=True)
    # collection.sort(reverse=True, key=tri_person)

    colect = collection
    if not first == -1:
        colect = collection[:first]
    quantite = len(colect)
    if quantite == 0:
    # Alternative     
    #if collection == ():
        print("-------------")
        print("AUCUNE PIZZA")
        print("-------------")
        return # avec le return ELSE pas necessaire
    #else:
    print(f"---- Liste des PIZZAS ({quantite}) ----")
    for i in colect:
        print(" - ", i) 
    print()
    print("Premiere Pizza : ", colect[0])
    print()
    print("Derniere Pizza : ", colect[-1])



    
def pizza_existe(pizzas, nouvelle):
    for pizza in pizzas:
        if pizza == nouvelle:
            return True
    return False


pizzas = ["4 fromages", "Vegetarienne", "Hawaii", "Calzone"]

ajouter_pizza(pizzas)
afficher(pizzas, 3)

#print(pizza_existe(pizzas, "vegetarienne"))


#vide = ()

#afficher(vide)
#afficher(pizzas)
