
class Pizza:
    def __init__(self, nom, prix, ingredients, vege=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vege = vege
    def Afficher(self):
        veget = ""
        if self.vege:
            veget = " - VEGETARIENNE"
        print(f"Pizza : {self.nom} - Prix : $ {self.prix} {veget}")
        print(f"Ingredients ({len(self.ingredients)}) ")
        print(", ".join(self.ingredients))
        print()
     
#Classe Pizza personnalisee

class PizzaPersonnalisee(Pizza):
    PRIX_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    dernier_numero = 0
    def __init__(self):
        PizzaPersonnalisee.dernier_numero += 1
        self.numero = PizzaPersonnalisee.dernier_numero
        super().__init__(f"Personalisee {self.numero}", 0, [])
        self.demander_ingredients()
        self.calculer_prix()


    def demander_ingredients(self):
        print()
        print(f"Ingredients pour la pizza personnalisee {self.numero}")
        while True:
            ingredient = input("Entrer un ingredient (ou ENTER pour terminer : ")
            if ingredient == "":
                return 
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingredient(s) : {', '.join(self.ingredients)}")

    def calculer_prix(self):
        nb_ingredients = len(self.ingredients)
        self.prix = self.PRIX_BASE + (nb_ingredients * self.PRIX_PAR_INGREDIENT)






# pizza1 = Pizza("4 Fromages", 8.5, ("peperonni", "brie", "elemental", "parmesan"))
# pizza1.Afficher()

pizzas =  [
            Pizza("4 Fromages", 8.5, ("peperonni", "brie", "elemental", "parmesan"), True),
            Pizza("Vegetarienne", 11, ("mozarella", "champignons", "poivron vert", "tomates"), True),
            Pizza("Ecrevisses", 13, ("ecrevisses", "tomates", "huile olive", "parmesan")),
            Pizza("Peperonni", 9.5, ("peperonni", "olives noires", "elemental", "champignons"), True),
            Pizza("Hawai", 12, ("peperonni", "jambon", "ananas", "mozarella", "origan", "tomates")),
            PizzaPersonnalisee(),
            PizzaPersonnalisee()

        ]     


# for pizza in pizzas:
#     if not pizza.vege: # pizza non vegetariennes
#         pizza.Afficher()


# Seulement avec tomates dans ingredients
# for pizza in pizzas:
#     if "tomates" in pizza.ingredients:
#         pizza.Afficher()


# Moins de $ 10
# for pizza in pizzas:
#     if pizza.prix < 10:
#         pizza.Afficher()


#Trier pizza
#Peut pas appeler sort sur tuple. Transformer en liste


# def tri(e): # Tri sur nom
#     return e.nom

def tri(e):
    return len(e.ingredients)

#pizzas.sort(key=tri, reverse=True)

for pizza in pizzas:
    pizza.Afficher()
