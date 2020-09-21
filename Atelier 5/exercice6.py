# Auteur(s) : MACRE Alexis
# Date : 21/09/2020
# Version : 1.0
# Description : Atelier de programmation 5 Exo 6 Python

from random import *
import matplotlib.pyplot as plt
import numpy as np
import time

from exercice1 import gen_list_random_int


def sort_list(liste_a_trier:list)->list:
     """Fonction de tri par ordre croissant d'une liste d'entiers.
     
     Arguments:
     liste_a_trier -- liste que l'on souhaite trier
     
     Retourne liste_croissant, la liste avec les nombres triés par ordre croissant
     """
     liste_copie = liste_a_trier[:]
     liste_croissant = []

     while liste_copie != []:
          minimum = min(liste_copie)
          index_min = liste_copie.index(minimum)
          liste_croissant.append(minimum)
          del liste_copie[index_min]
     
     return liste_croissant

def perf_mix(fonction1:callable,fonction2:callable,liste_tailles:list,nbr_execs:int)->tuple:
     """Fonction de mesure de comparaison durée d'execution entre deux fonctions.
     Calcule la moyenne de temps d'execution pour chacune des tailles et en fait une liste (liste_moyennes)

     Arguments:
     fonction1      -- la première fonction dont on souhaite mesurer le temps d'execution
     fonction2      -- la seconde fonction
     liste_tailles  -- liste contanant les tailles des list[int] avec lesquelles on souhaite tester les fonctions
     nbr_execs      -- nombre d'executions pour calculer la moyenne
     
     Retourne le couple (resultat_fonction1,resultat_fonction2) 
     avec resultat_fonction sous la forme (liste_tailles,liste_moyennes)
     """
     
     fonctions = [fonction1,fonction2]
     retour_final = [None,None]     
     numero_fonction = 0

     for fonction in fonctions:
          liste_moyennes = []
          somme_temps = 0
          for taille in liste_tailles:
               for i in range(1,nbr_execs):
                    temps_debut = time.perf_counter()
                    fonction(gen_list_random_int(taille))
                    temps_fin = time.perf_counter()

                    temps_ecoule = temps_fin-temps_debut
                    somme_temps+=temps_ecoule
               liste_moyennes += [somme_temps/nbr_execs]
               
          retour_final[numero_fonction]=(liste_tailles,liste_moyennes)
          numero_fonction+=1

     return (retour_final[0],retour_final[1])

resultats = perf_mix(sort_list,sorted,[100,500,1000],100)

fig, ax = plt.subplots()

ax.plot(resultats[0][0],resultats[0][1],label="extract_elements_list")

ax.plot(resultats[1][0],resultats[1][1],label="sample")

ax.legend(loc="upper center",shadow=True, fontsize='x-large')

plt.show()