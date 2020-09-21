from random import *
from exercice1 import gen_list_random_int
from exercice2 import mix_list
import time

def moyenne_temps_exec(fonction:callable,params:list,nbr_execs:int=10)->float:
     """Fonction de mesure de durée d'execution d'une fonction.
     
     Arguments:
     fonction -- la fonction dont on souhaite mesurer le temps d'execution
     params   -- liste des parametres avec lesquels on souhaite executer la fonction
     
     Retourne la moyenne des temps d'execution mesurés
     """

     somme_temps = 0.0

     for i in range(1,nbr_execs):
          temps_debut = time.perf_counter()
          fonction(params)
          temps_fin = time.perf_counter()

          temps_ecoule = temps_fin-temps_debut
          somme_temps+=temps_ecoule

     

     return somme_temps/nbr_execs

mega_liste = gen_list_random_int(3000,0,80)

print(moyenne_temps_exec(mix_list, mega_liste))
print(moyenne_temps_exec(shuffle,mega_liste))

     

