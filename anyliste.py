def chaine_contient_chiffre(chaine):
    for c in chaine:
        if c.isdigit():
            return True
    return False

noms = ["Maria", "Sophia", "Alyssa", "Christophe", "Zoe",] 

a = [True, True, False, False]
print(any(a)) # Si au moins 1 elements est True return True
print(all(a)) # Pour etre True tous les elements doivent etre True

avec_a = [True if "a" in nom.lower() else False for nom in noms]
print(avec_a)
print(any(avec_a))
print(all(avec_a)) 
print("-----------")
# si Chaine contient chiffre

# nom = input("Quel est ton nom : ")
# if nom == "":
#     print("Le nom ne peut pas etre vide.")
# elif chaine_contient_chiffre(nom):
#     print("Nom invalide, peut pas contenir de chiffres")
# else:
#     print("Bonjour", nom)

# ou encore
nom = "toto12"

digits = [c.isdigit() for c in nom] # return liste tous char contenant un chiffre true or False

contient_un_chiffre = any([c.isdigit() for c in nom])
print(digits)
print(contient_un_chiffre)
