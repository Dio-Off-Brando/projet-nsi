##################
#   jeu de nim   #
#     Mehdi      #
#       &        #
#                #
#                #
##################




def affichage_tas(liste):
    pass

def choix_allumettes():
    return input("choisis un nombre d'allumettes: ")

def choix_tas():
    return input("choisis un tas")


def affichage_allumettes(liste):
    pass


# fonction initialisation

def initialisation(liste=[1,2,3,4,5,6], liste2=[1,2,3,4,5,6]):
    joueur1=input("nom joueur1: ")
    joueur2=input('nom joueur2: ')
    total_alu=0
    for i in range(liste):
        total_alu = total_alu+ liste[i]*liste2[i]
    
    #retourner une liste avec les donnees [joueur1, joueur2, liste ,liste2, total_alu]
    return [joueur1, joueur2, liste, liste2, total_alu]


#fonction principale

def main():
    joueur1, joueur2, liste, liste2, total_alu = initialisation()
    
    dernier_joueur = ""
    while total_alu <0:
        affichage_tas()
        affichage_allumettes()
        tas = choix_tas()
        nb_alu = choix_allumettes()

        
