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


from asyncio import QueueEmpty


def demander_reponse_numerique_utlisateur(min, max):
    reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int

        print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
    except:
        print("ERREUR : Veuillez rentrer uniquement des chiffres")
    return demander_reponse_numerique_utlisateur(min, max)
    

'''
titre = question[0]
choix = question[1]
bonne_reponse = question[2]
'''
def poser_question(question):
    # titre_question, r1, r2, r3, r4, choix_bonne_reponse
    choix = question[1]
    bonne_reponse = question[2]
    print("QUESTION")
    print("  " + question[0])
    for i in range(len(choix)):
        print("  ", i+1, "-", choix[i])

    print()
    resultat_response_correcte = False
    reponse_int = demander_reponse_numerique_utlisateur(1, len(choix))
    if choix[reponse_int-1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        resultat_response_correcte = True
    else:
        print("Mauvaise réponse")
        
    print()
    return resultat_response_correcte


'''
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France ?"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"

'''

def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print("Score final :", score, "sur", len(questionnaire))

questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

# lancer_questionnaire(questionnaire)

class Questionnaire:
    def __init__(self, questions):
        self.questions = questions
        print("DEMARRER QUESTIONNAIRE")    

    def lancer(self):
        score = 0
        for question in self.questions:
            if question.Poser_question():
                score += 1
        print("Score final : ", score, "sur", len(self.questions))
        return score 


class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def FromData(data):
        q = Question(data[2], data[0], data[1])
        return q


    def Poser_question(self):
        print("Question")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print(f"  {i+1} - {self.choix[i]}")
        print()
        resultat_reponse = False
        reponse_int = Question.demander_reponse_numerique(1, len(self.choix))
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower():
            print("Bonne Reponse !")
            resultat_reponse = True
        else:
            print("Mauvaise Reponse !")
        print()
        return resultat_reponse


    def demander_reponse_numerique(min, max):
        reponse_str = input(f"Votre Reponse entre {min} et {max} : ")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int
            print(f"Vous devez entrer un nombre entre {min} et {max}.")
        except:
            print("ERREUR : Vous devez entrer un chiffre.")
        return demander_reponse_numerique_utlisateur(min, max)



q1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
q2 = ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")
q3 = ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
        

question1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
question2 = Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")
question3 = Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
# question1.Poser_question()
# question2.Poser_question()
# question3.Poser_question()
# print(a)

questions = (
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
    Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
)
questionnaire = Questionnaire(questions)
# questionnaire.lancer()

data = (("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris", "Quelle est la capitale de la France ?")

q = Question.FromData(data)
q.Poser_question()
