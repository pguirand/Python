import random

def demander_nombre(nb_min, nb_max):
    nb_int = 0
    while nb_int == 0:
        nb_str = input(f"quel est le nombre entre {nb_min} et {nb_max} ?")
        try:
            nb_int = int(nb_str)
        except:
            print("ERREUR : Vous devez rentrer un nombre, reessayer")
        else:
            if nb_int < nb_min or nb_int > nb_max:
                print(f"Erreur. dsoit etre compris entre {nb_min} et {nb_max}.")
                nb_int = 0
    return nb_int



NB_MIN = 1
NB_MAX = 10
NB_MAG = random.randint(NB_MIN, NB_MAX)
NB_VIES = 4

# vies = NB_VIES
# nombre = 0
# while not nombre == NB_MAG and vies > 0:
#     nombre = demander_nombre(NB_MIN, NB_MAX)
#     if nombre < NB_MAG:
#         print("le nombre magique est plus grand")
#         vies -= 1
#     elif nombre > NB_MAG:
#         print("le nombre magique est plus petit")
#         vies -= 1
#     else:
#         print("Bravo vous avez gagne !")

# if vies == 0:
#     print("Vous avez perdu")

#for loop
gagne = False
for i in range(0, NB_VIES):
    vies = NB_VIES - i
    print(f"il vous reste {vies} vies")
    nombre = demander_nombre(NB_MIN, NB_MAX)
    if nombre < NB_MAG:
        print("le nombre magique est plus grand")
    elif nombre > NB_MAG:
        print("le nombre magique est plus petit")
    else:
        print("Bravo vous avez gagne !")
        gagne = True
        break

if not gagne:
    print("Vous avez perdu")
