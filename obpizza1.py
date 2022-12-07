class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne:bool=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne
        
    def Afficher_pizza(self):
        vege = ""
        if self.vegetarienne:
            vege = "- VEGETARIENNE"
        print(f"PIZZA {self.nom} : $ {self.prix} {vege}")
        print(", ".join(self.ingredients))
        print()
        # return self.nom, self.prix, self.ingredients

class Personnalisee_Pizza(Pizza):
    PRIX_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    dernier_numero = 0  
    def __init__(self):
        Personnalisee_Pizza.dernier_numero += 1
        self.numero = Personnalisee_Pizza.dernier_numero
        super().__init__(f"Personnalisee {self.numero}", 0, [])
        self.rentrer_ingredients()
        self.calculer_prix()

    def rentrer_ingredients(self):
        print(f"Ingredienets pour Pizza Personnalisee No {self.numero}")
        while True:
            ingredient = input("Ajouter un ingredient : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingredient(s): {', '.join(self.ingredients)}")

    def calculer_prix(self):
        self.prix = self.PRIX_BASE + len(self.ingredients)*self.PRIX_PAR_INGREDIENT

pizza1 = Pizza("Hawaii", 8.5, ('Ananas', 'Olives', 'Champignons', 'tomates'), True)
pizza2 = Pizza("Bacon", 11.5, ('Bacon', 'Mozarella', 'ail', 'oignons'))
pizza3 = Pizza("Lakay", 12.5, ('Hareng', 'Olives', 'Griot', 'tomates'))
pizza4 = Pizza("Vegetarien", 8, ('oignons', 'Parmesan', 'Letues', 'tomates'), True)
pizza5 = Pizza("Peperroni", 10.5, ('Peperroni', 'Parmesan', 'Champignons'))
personnalisee1 = Personnalisee_Pizza()
personnalisee2 = Personnalisee_Pizza()


menu = [pizza1, pizza2, pizza3, pizza4, pizza5, personnalisee1, personnalisee2]
for pizza in menu:    
    pizza.Afficher_pizza()



# for pizza in menu:
#     if not pizza.vegetarienne:
#         pizza.Afficher_pizza()

# # pizza1.Afficher_pizza()
# print("Avec tomates")

# for pizza in menu:
#     if not "tomates" in pizza.ingredients:
#         pizza.Afficher_pizza()

# print("Prix moins de 10")
# for pizza in menu:
#     if pizza.prix < 10:
#         pizza.Afficher_pizza()

# def tri(p):
#     # return p.prix
#     return len(p.ingredients)

# menu.sort(key=tri)
# print("Trier Pizzas")
