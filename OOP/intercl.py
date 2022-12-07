import random

list = []
text = ""
n1 = int(input("Entrer le premier intervalle (0-100 : "  ))
n2 = int(input("Entrer le second intervalle (0-100 : "))

for i in range(n1,n2+1):
    list.append(i)
    #text = text +","+ str(i)
    text = f"{text},{i}"

spli = text.split(",")
fspli = text[1:]
#print(fspli)
flist = fspli.split(",")
#print(flist)

#
# Ou plus simple 

print(list)

class Start():
    
    def __init__(self):
        print("Distributing list...")
        self.allnumb = list

    def repartir(self):
        print("Repartition aleatoire...")
        l = len(list)
        self.repart = random.sample(list, l)
        return self.repart
        

class Paquet():

    def __init__(self,lot):
        self.lot = lot
        print("INITIALIATION PAQUET...")
    
    def nouveau(self):
        print("PRINT FORMAT...")
        lg = len(self.numeros)
        r = lg % 2
        if r != 0:
            lg -= 1

        half = int(lg / 2)
        self.new_list = random.sample(self.numeros, half)
        return self.new_list
        
        

    def retirer(self):
        pass
        
    

class Joueur():
    
    def __init__(self,nom,main):
        self.nom = nom
        self.main = main

    def tirer(self):
        pass


    
lancer = Start()
val = lancer.repartir()
print(f"La liste aleatoire est :\n{lancer.repartir()}")
ouverture = Paquet()




