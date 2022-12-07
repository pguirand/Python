import random
#from random import shuffle

articles = 'bycicle,voiture,telephone,laptop,TV,AC'

list_art = articles.split(',')

list_prix = []


for i in range(len(list_art)):
    numb = random.randint(200,1000)
    list_prix.append(numb)
    print(list_prix)


print(list_art)
print(list_prix)

class Board():
    """
    Tableau d'affichage des Articles et Prix associes
    """

    def __init__(self):
        print('Assigning Prices...\n\n')
        self.glist = [(list_art[i], list_prix[i]) for i in range(0,len(list_art))]
        #return glist
        

    def distrib(self):

        print("Assignation des articles")
        l = len(self.glist)
        print(self.glist)
        print(f"Longueur liste initiale : {l}")
        slist = 10
        self.s_list = random.sample(self.glist,l)
        return self.s_list
        print(f"Liste shuffled\n{s_list}")

    def split(self):
        print('SPLITTING...')
        return (self.s_list[:3],self.s_list[3:])

       
        
class Joueur():
    '''
    Cette classe contient les actions Human et AI pour
    jouer. Entrer les montant jusqua ce que jeu est 
    termine
    '''
    def __init__(self,name,jliste):
        self.name = name
        self.jliste = jliste
        print("Classe Joueurs")
        #return self.name
    
    def __str__(self):
        pass
        return f"Le joueur {self.name} a la liste {self.jliste}"


play = Board()

play.distrib()

portionA,portionB = play.split()
print(f"{portionA}\n{portionB}")

util = input("Entrer le nom du joueur : ")
mliste = "1 2 3"


jcl = Joueur(util,mliste)

print(jcl.name)
print(jcl.jliste)

print("GAME START...")

print(f"{util} a votre tour...")
print(f"Liste des articles a choisir :")
for i in range(1,4):
    print(f"{i} : {portionA[i-1][0]}")


choix = int(input("Entrer votre choix : "))
    
while choix < 1 or choix > 3:
    choix = int(input(f"{choix} : Intervalle non correspondant, Ressayer :"))











































































 # new_list = []
        # while l != 0 :
        #     #print(f"Longueur in loop {l}")
        #     s = random.randint(0,l-1)
        #     #print(f"corresponding random value {s}")
        #     r = self.glist.pop(s)
        #     #print(r)
        #     new_list.append(r)
        #     #print(self.glist)
        #     l = len(self.glist)
        # print(new_list)
            
         
        
        # for i in range(0,len(self.glist)):
        #     r = self.glist.pop()
        #     print(r)
        #     print(f"{self.glist}\n")