# Auteur(s) : MACRE Alexis
# Date : 21/09/2020
# Version : 1.0
# Description : Atelier de programmation 5 Exo 2 Python

from random import randint

def mix_list(list_to_mix:list)->list:
     """Prend une liste et mélange ses élements
     
     Arguments:
     list_to_mix -- la liste à mélanger
     
     Retourne liste_retour, la liste mélangée
     """
     liste_retour = list_to_mix[:]
     taille = len(list_to_mix)

     for i in range(taille):
          random=randint(0,taille-1)
          liste_retour[i],liste_retour[random] = liste_retour[random],liste_retour[i]

     return liste_retour

#for i in range(10):
     #print(mix_list([2,2,5,585,78,952,523,2355,414]))
