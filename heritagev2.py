
#methode de classe ou methode statique appeler une fonction simple dans la classe
#Personne.autrefonction()
#methode d'instance appelle fonction a partir d'instance

#POO ->
#Definition

# Etre Vivant           :   Classe parent
# Chat  Personne        :   Classen enfant(Classe derivees)       

class EtreVivant:
    ESPECE_ETRE_VIVANT = "(Etre vivant non identifie)"
    
    def AfficherInfoEtreVivant(self):
        print("Info Etre Vivant : " + self.ESPECE_ETRE_VIVANT)

class Chat(EtreVivant):
    ESPECE_ETRE_VIVANT = "Chat (Mammifere Felin)"


class Personne(EtreVivant):
    ESPECE_ETRE_VIVANT = "Humain (Homo Sapiens)"

    def __init__(self, nom="", age=0):
        self.nom = nom # Creer une variable d'instance : nom
        self.age = age
        if nom == "":
            self.entrer_nom()
        print(f"Constructeur personne, {self.nom}")

    def est_majeur(self):
        return self.age >=18

    def se_presenter(self):    
        infos = "Bonjour, je m'appelle "+ self.nom
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

class Etudiant(Personne):
    def __init__(self, nom:str, age:int, etudes:str):
        super().__init__(nom, age)
        self.etudes = etudes

    def se_presenter(self): # surcharger la methode
        super().se_presenter() # appeler se presenter de classe parente
        print("je suis etudiant en "+self.etudes)    

#
    



#Utilisation

liste_personnes = [Personne("Jean", 28), 
                    Personne("Pierre", 15),
                    Personne("Emmanuel", 25)
]
liste_personnes[0].ESPECE_ETRE_VIVANT = "Mutant"

for personne in liste_personnes:
    personne.se_presenter()
    # personne.afficher_infos_etre_vivant()
    personne.AfficherInfoEtreVivant()
    print()

chat = Chat()
chat.AfficherInfoEtreVivant()
etrevivant = EtreVivant()
etrevivant.AfficherInfoEtreVivant()

etudiant = Etudiant("Junior", 15, "Sciences")
etudiant.se_presenter()
etudiant.AfficherInfoEtreVivant()

