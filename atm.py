
balance = float(600)

choix = [1, 2, 3]
print("1:Balance | 2:Retrait | 3:Depot")



    
def atm():
    essaie = 0
    
    while True:
        operation = int(input("le type d'operation : \n"))
        if not 1 <= operation <= 3:
            print("Choisir entre 1 et 3 Retry.")
            essaie += 1
            if essaie == 3:
                print("Fin Operation. 3 Essais")
                break
        elif operation != 1:
            ptries = 1
            while True:
                print(f"Le solde actuel est: {balance} USD\n")
                if operation == 2:
                    transac = "retrait"
                else:
                    transac = "depot"
                print(f"OPERATION EN COURS ... {transac.upper()}\n")
                montant = float(input("Montant transaction : "))
                if montant < 0:
                    print(f"can't be negative, retry. Essaie {ptries}")
                    ptries += 1
                    if ptries == 4:
                        print("Too many attempts")
                        return    
                elif montant > 2000:
                    if operation == 2:
                        print("impossible")
                        return
                elif montant > balance:
                    if operation == 2:
                        print("Ret can't be over solde")
                        return
                else:
                    if not montant % 5 == 0 and operation == 2:
                        print("Should be multiple of 5 ")
                        return
                    else:
                        break
                break

            
            val = montant
            if operation == 2:
                print(f"OPERATION {transac.upper()}")
                val = val * - 1
                break
            elif operation == 3:
                print(f"OPERATION {transac.upper()}")
                break
        else:
            val = 0
            break
    
    new_bal = balance + val - 0.5
    if operation != 1:
        print(f"{transac.upper()} effctue avec succes !\n")
        print(f"un {transac} de : {montant} USD.\nLe nouveau solde est : {new_bal} USD")
    else:
        print("\nSOLDE")
        print("#########\n")
        print(f"Verfication solde : {balance}")


atm()