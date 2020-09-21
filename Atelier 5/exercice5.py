# Auteur(s) : MACRE Alexis
# Date : 21/09/2020
# Version : 1.0
# Description : Atelier de programmation 5 Exo 5 Python

from random import *
import matplotlib.pyplot as plt
import numpy as np
import time

from exercice1 import gen_list_random_int
from exercice2 import mix_list
from exercice4 import extract_elements_list

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

def perf_mix2(fonction1:callable,fonction2:callable,liste_tailles:list,nbr_extract:int,nbr_execs:int)->tuple:
     """Fonction de mesure de comparaison durée d'execution entre deux fonctions.
     Calcule la moyenne de temps d'execution pour chacune des tailles et en fait une liste (liste_moyennes)

     Arguments:
     fonction1      -- la première fonction dont on souhaite mesurer le temps d'execution
     fonction2      -- la seconde fonction
     liste_tailles  -- liste contanant les tailles des list[int] avec lesquelles on souhaite tester les fonctions
     nbr_extract    -- parametre de la fonction extract_elements_list que l'on doit spécifier
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
                    fonction(gen_list_random_int(taille),nbr_extract)
                    temps_fin = time.perf_counter()

                    temps_ecoule = temps_fin-temps_debut
                    somme_temps+=temps_ecoule
               liste_moyennes += [somme_temps/nbr_execs]
               
          retour_final[numero_fonction]=(liste_tailles,liste_moyennes)
          numero_fonction+=1

     return (retour_final[0],retour_final[1])


# resultats = perf_mix2(extract_elements_list,sample,[100,500,1000],100,100)
# resultats = perf_mix(mix_list,shuffle,[100,500,1000],100)

# fig, ax = plt.subplots()

# ax.plot(resultats[0][0],resultats[0][1],label="extract_elements_list")

# ax.plot(resultats[1][0],resultats[1][1],label="sample")

# ax.legend(loc="upper center",shadow=True, fontsize='x-large')

# plt.show()

     

