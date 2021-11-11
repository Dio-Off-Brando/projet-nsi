##################
#   jeu de nim   #
#     Mehdi      #
#    Antoine     #
#     Mathys     #
#                #
##################
example=[1,2,3,4,5,6]


#au lieu de faire des if avec des valeur et de verifier si la valeur choisise par la joueur est entre 1 et 3, on limite simplement le choix du joueur a prendre que 1, 2, et 3

def affichage_tas(liste):
  nb_tas=len(liste)
  string_presentation=""
  for i in range(len(liste)):
      string_presentation+= "|  "+str(i+1)+"  "
  print(string_presentation)



def choix_allumettes(joueur, liste, tas):
    #adapté au nom du joueur
    # limiter le joueur a prendre seulement des chiffres
    chiffres= "123"
    nbAlu=input("À " + joueur + " de choisir un nombre d'allumettes : ")
    while nbAlu  not in chiffres and  liste[tas-1]-nbAlu <=0:
       nbAlu= input("erreur: valeur invalide, choisis une autre valeur : ")
    return int(nbAlu)


def choix_tas(joueur, liste):
    #adapté au nom du joueur
    chiffres = "123456"
    tas = input("À " + joueur + " de choisis un tas : ")
    while tas not in chiffres and liste[tas]==0:
      tas = input("choix invalide, choisis une autre valeur : ")
    return int(tas)-1



def affichage_allumettes(liste):
  resultat = ""
  for i in liste : 
      for k in range(i+1) :
        resultat+= "I"*k
      resultat+= " "*(6-i)
  print(resultat)
               


# fonction initialisation
#"""liste_allumettes=[1,2,3,4,5,6])"""
def initialisation(liste):
    joueur1=input("nom du joueur 1 : ")
    joueur2=input("nom du joueur 2 : ")
    total=0
    for i in liste:
      total += i 
    #retourner une liste avec les donnees [joueur1, joueur2, liste_tas , total_alu]
    return [joueur1, joueur2, total, liste]


#fonction principale

def main(liste_tas=[1, 2, 3, 4, 5, 6]):
    joueur1, joueur2, total_alu, liste = initialisation(liste_tas)
    # 0 veut dire joueur1, 1 veut dire joueur2
    # mis a 1 pour commencer avec le joueur1
    liste = liste
    dernier_joueur = 1
    joueur=0

    while total_alu >0:
        #choisit le premier joueur
        if dernier_joueur==1:
            nom_joueur=joueur1
            dernier_joueur = 0
        #choisit dernier joueur
        else:
            nom_joueur = joueur2
            dernier_joueur=1

        #méchanique tour    
        affichage_tas(liste_tas)
        #affichage_allumettes(liste_tas)
        print(liste)
        print(total_alu)

        tas = choix_tas(nom_joueur, liste)
        nbAlu = choix_allumettes(nom_joueur, liste, tas)
        liste[tas] = liste[tas]-nbAlu
        total_alu -= nbAlu
        
#main()
