# Auteur(s) : MACRE Alexis
# Date : 21/09/2020
# Version : 1.0
# Description : Atelier de programmation 5 Exo 6 Python

from random import *
import matplotlib.pyplot as plt
import numpy as np
import time
from exercice5 import perf_mix

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



resultats = perf_mix(sort_list,sorted,[100,500,1000],100)

fig, ax = plt.subplots()

ax.plot(resultats[0][0],resultats[0][1],label="sort_list")

ax.plot(resultats[1][0],resultats[1][1],label="sorted")

ax.legend(loc="upper center",shadow=True, fontsize='x-large')

plt.show()