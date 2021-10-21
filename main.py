##################
#   jeu de nim   #
#     Mehdi      #
#    Antoine     #
#     Mathys     #
#                #
##################




def affichage_tas(liste):
    nb_tas=len(liste)
    string_presentation=""
    for i in range(len(liste)-1):
      string_presentation+= "|    "
     

def choix_allumettes(joueur):
    #adapté au nom du joueur
    return int(input(joueur+" choisis un nombre d'allumettes : "))


def choix_tas(joueur):
    #adapté au nom du joueur
    return int(input("à " + joueur+"de choisis un tas : "))


def affichage_allumettes(liste):
    pass


# fonction initialisation
#"""liste_allumettes=[1,2,3,4,5,6])"""
def initialisation():
    joueur1=input("nom du joueur 1 : ")
    joueur2=input("nom du joueur 2 : ")
    total_alu=0
    for i in range(len(liste_tas)):
        total_alu +=len(liste_tas[i])
    
    #retourner une liste avec les donnees [joueur1, joueur2, liste_tas , total_alu]
    return [joueur1, joueur2, liste_tas, total_alu]


#fonction principale

def main(liste_tas=["I", "II", "III", "IIII", "IIIII", "IIIIII"]):
    joueur1, joueur2, liste_tas, total_alu = initialisation(liste_tas)
    # 0 veut dire joueur1, 1 veut dire joueur2
    # mit a 1 pour commencer avec le joueur1
    dernier_joueur = 1
    joueur=0

    while total_alu >0:
        #choisis le premier joueur
        if dernier_joueur==1:
            nom_joueur=joueur1
            dernier_joueur = 0
        #choisis dernier joueur
        else:
            nom_joueur = joueur2
            dernier_joueur=1

        #mécanique tour    
        affichage_tas(liste_tas)
        affichage_allumettes(liste_tas)
        tas = choix_tas(nom_joueur)
        nb_alu = choix_allumettes(nom_joueur)
        # enlever nb_alu de tas
        liste_tas[tas] = liste_tas[tas][:nb_alu] #enlève nb_alu de char à liste_tas[tas]

        
