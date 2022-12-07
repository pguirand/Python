from xml.dom.pulldom import PROCESSING_INSTRUCTION


class EtreVivant:
    ESPECE_ETRE_VIVANT = "Etre Vivant non identifie"

    def AfficherInfosEtreVivant(self):
        print("Infos : ", self.ESPECE_ETRE_VIVANT)


    


class Personne(EtreVivant):
    ESPECE_ETRE_VIVANT = "Etre Humain "

    def __init__(self, nom:str="", age:int=0):
        self.nom = nom
        self.age = age
        if nom == "":
            self.demander_infos()
        print("Constructeur Personne : ", self.nom)

    def EstMajeur(self):
        return self.age >= 18

    def SePresenter(self):
        print("Bonjour, je m'appelle", self.nom)
        if self.EstMajeur():
            print("je suis majeur")
        else:
            print("je suis mineur")

    def demander_infos(self):
        self.nom = input("Entrer votre nom : ")

    def AfficherInfosEtreVivant(self):
        print("Infos : ", self.ESPECE_ETRE_VIVANT)
        print()

class Chat(EtreVivant):
    ESPECE_ETRE_VIVANT = "Mammifere - Chat"

    def AfficherInfosEtreVivant(self):
        print("Infos : ", self.ESPECE_ETRE_VIVANT)

class Etudiant(Personne):
    def __init__(self, nom:str="", age:int=0, etudes:str=""):
        super().__init__(nom, age)  
        self.etudes = etudes

    def SePresenter(self):
        super().SePresenter()
        print("J'etudie les ", self.etudes)
    


etrevivant = EtreVivant()
etrevivant.AfficherInfosEtreVivant()

personne1 = Personne("Jean", 12)
personne1.SePresenter()
personne1.AfficherInfosEtreVivant()

personne2 = Personne(age=19)
personne2.SePresenter()
personne2.AfficherInfosEtreVivant()

chat = Chat()
chat.AfficherInfosEtreVivant()

etudiant = Etudiant("Pierre", 25, "Sces informatiques")
etudiant.AfficherInfosEtreVivant()
etudiant.SePresenter()