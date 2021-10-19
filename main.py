##################
#   jeu de nim   #
#     Mehdi      #
#       &        #
#                #
#                #
##################




def affichage_tas(liste):
    pass

def choix_allumettes(joueur):
    #adapté au nom du joueur
    return int(input(joueur+" choisis un nombre d'allumettes: "))


def choix_tas(joueur):
    #adapté au nom du joueur
    return int(input("à " + joueur+"de choisis un tas : "))


def affichage_allumettes(liste):
    pass


# fonction initialisation

def initialisation(liste=[1,2,3,4,5,6], liste2=[1,2,3,4,5,6]):
    joueur1=input("nom du joueur 1: ")
    joueur2=input('nom du joueur 2: ')
    total_alu=0
    for i in range(len(liste)):
        total_alu = total_alu+ liste[i]*liste2[i]
    
    #retourner une liste avec les donnees [joueur1, joueur2, liste ,liste2, total_alu]
    return [joueur1, joueur2, liste, liste2, total_alu]


#fonction principale

def main():
    joueur1, joueur2, liste, liste2, total_alu = initialisation()
    # 0 veut dire joueur1, 1 veut dire joueur2
    # mit a 1 pour commencer avec le joueur1
    dernier_joueur = 1
    joueur=0

    while total_alu >0:
        if dernier_joueur==1:
            nom_joueur=joueur1
            dernier_joueur = 0
        else:
            nom_joueur = joueur2
            dernier_joueur=1
        affichage_tas(liste)
        affichage_allumettes(liste2)
        tas = choix_tas(nom_joueur)
        nb_alu = choix_allumettes(nom_joueur)
        # enlever nb_alu de tas
        liste2[tas]-=nb_alu
      

        
