

class Personne:
    def __init__(self, nom:str="", age:int=0):
        self.nom = nom  
        self.age = age
        if nom == "":
            self.demander_infos()      
        print("Construction Personne", self.nom)

    def estMajeur(self):
        return self.age >=18


    def Se_Presenter(self):
        infos = "Bonjour, Je m'appelle " + self.nom
        if self.age ==0:
            print(infos)
        else:
            print(infos,". j'ai", self.age, "ans.")
            if self.estMajeur():
                print("je suis majeur")
            else:
                print("Je suis mineur")
    
    def demander_infos(self):
        self.nom = input("Entrer votre nom : ")
        

# personne2.nom = "Eric"

personne1 = Personne("Pierre", 15)
personne1.Se_Presenter()
personne2 = Personne("Jean", 38)
personne2.Se_Presenter()
personne3 = Personne()
personne3.Se_Presenter()
