
'''def afficher_infos(nom, age):
    print(f"La personne s'appelle {nom} et a {age} ans.")

def demander_nom_personne():
    return input("Quel est votre nom : ")

nom1, nom2 = "Jean", "Pierre"
age1, age2, age3 = 25, 35, 18

afficher_infos(nom1, age1)
afficher_infos(nom2, age2)

nom3 = demander_nom_personne()
afficher_infos(nom3, age3)'''

#methode de classe ou methode statique appeler une fonction simple dans la classe
#Personne.autrefonction()
#methode d'instance appelle fonction a partir d'instance

#POO ->
#Definition
class Personne:
    def __init__(self, nom="", age=0):
        self.name = nom # Creer une variable d'instance : nom
        self.age = age
        if nom == "":
            self.entrer_nom()
        print(f"Constructeur personne, {self.name}")

    def est_majeur(self):
        return self.age >=18
        # if self.age >= 18:
        #     return True
        # return False

    def se_presenter(self):    
        infos = "Bonjour, je m'appelle "+ self.name
        if self.age !=0:
            infos += ", j'ai "+ str(self.age) + "ans."  
        print(infos)
        if self.age !=0:
            if self.est_majeur():
                print("Je suis majeur")
            else:
                print("je suis mineur")

    def entrer_nom(self):
        self.name = input("Entrer Votre nom : ")


#Utilisation
personne1 = Personne("Jean", 28)
personne2 = Personne("Pierre", 15)
personne1.se_presenter()
personne2.se_presenter()
# personne2 = Personne("Toto")
print(personne2.name)
personne3 = Personne()
personne3.se_presenter()

