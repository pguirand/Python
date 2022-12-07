
CMP = 0.394
PCM = 2.54

def convertir():
    choix_int = 0
    while choix_int == 0:
        print(("Choisir l'unite de conversion.").upper())
        print("1 : Convertir cm en pouces\n2 : Convertir pouces en cm")
        choix_str = input("Quel est votre choix (1 ou 2) : ")

        try: 
            choix_int = int(choix_str)
        except ValueError:
            print(("Vous devez entrer un nombre. ").upper())
            print()
        else:
            if choix_int not in [1,2]:
            # if (choix_int !=1 ) and (choix_int !=2):
                print(("Le choix doit etre obligatoirement 1 ou 2 !").upper())
                print()
                choix_int = 0
            else:
                if choix_int==1:
                    debut = "cm"
                    title = "Conversion cm en pouces... "
                    mult = CMP            
                    fin = "pouces"

                else:
                    debut = "pouces"
                    title = "Conversion pouces en cm..."
                    mult = PCM
                    fin = "cm"

    
    print("############")
    print(title.upper())
    val_str = input(f"Entrer le nombre de {debut} a convertir : ")
    
    try:
        val_float = float(val_str)
    except ValueError:
        print("Vous devez rentrer un float.")
    else:
        print(f"{title}\n{val_float} {debut} vaut {round(val_float*mult, 2)} {fin}.")
    return choix_int




convertir()