##################
#   jeu de nim   #
#     Mehdi      #
#    Antoine     #
#     Mathys     #
#                #
##################



#prend un argument comme [1,2,3,4,5]
def affichage_tas(liste):
    nb_tas=len(liste)
    string_presentation=""
    for i in range(len(liste)):
      string_presentation+= "|  "+str(i+1)+"  "
    return string_presentation



def choix_allumettes(joueur):
    
    #adapté au nom du joueur
    return int(input(joueur+" choisis un nombre d'allumettes : "))


def choix_tas(joueur):
    #adapté au nom du joueur
    return int(input("à " + joueur+"de choisis un tas : "))



# prend un argument comme ["I", "II", "III", "IIII", "IIIII"] 
def affichage_allumettes(liste):
    espace_alignement =6
    liste_reorganise_en_string =""
    for i in liste:
        liste_reorganise_en_string+= "| "+str(i)+" "*(espace_alignement-len(i))
    return liste_reorganise_en_string




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

    
