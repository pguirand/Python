# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions

def poser_question(question):
    result = False
    titre = question[0]
    choix = question[1]
    bonne_reponse = question[2]

    print("QUESTION")
    print(" ", titre)
    for i in range(len(choix)):
        print(f"  {i+1} - {choix[i]}")
    print()
    # reponse_str = input(f"Votre réponse (entre 1 et {len(choix)}) : ")
    # reponse_int = int(reponse_str)
    reponse_int = demander_input_numerique_user(1, len(choix))
    if choix[reponse_int-1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        # score += 1
        result = True
    else:
        print("Mauvaise réponse")
    
    print()
    return result

def demander_input_numerique_user(min, max):
    reponse_str = input(f"Votre réponse (entre {min} et {max}) : ")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int
        print(f"Chiffre doit etre compris entre {min} et {max}.")

    except ValueError:
        print("Vous devez rentrer un chiffre")
    return demander_input_numerique_user(min, max)





'''
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France ?"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"

'''

question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
question2 = ("Quelle est la capitale de la l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")
question3 = ("Quelle est la capitale d'Haiti ?", ("Jermie", "Cap-Haitien", "Jacmel", "Port-au-Prince"), "Port-au-Prince")


# poser_question(question1)
# poser_question(question2) 

questionnaire = (question1, question2, question3)
score = 0
for question in questionnaire:
    if poser_question(question):
        score += 1

# poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
#poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")

print("Score final :", score)