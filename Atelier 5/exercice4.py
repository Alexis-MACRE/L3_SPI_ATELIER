from random import randint
from exercice2 import mix_list

def extract_elements_list(list_in_which_to_choose:list,int_nbr_of_element_to_extract:int)->list:
     """Prend une liste et retourne n élements aléatoires de cette liste
     
     Arguments:
     liste_in_which_to_choose      -- liste dans laquelle on va prendre des éléments
     int_nbr_of_element_to_extract -- nombre d'éléments que l'on souhaite prendre de la liste
     
     Retourne liste_retour, la liste composée de int_nbr_of_element_to_extract élements aléatoires de list_in_which_to_choose 
     """
     liste_retour = []
     liste_random = mix_list(list_in_which_to_choose)

     for i in range(0,int_nbr_of_element_to_extract-1):
          liste_retour+=[liste_random[i]]

     return liste_retour

#for i in range(10):
     #print(extract_elements_list([2,2,5,585,78,952,523,2355,414],randint(2,10)))