from random import randint

def choose_element_list(list_in_which_to_choose:list):
     """Choisi un élément aléatoirement dans une liste
     
     Arguments:
     list_in_which_to_choose -- la liste dans laquelle on doit prendre un élément
     
     Retourne l'élement choisi aléatoirement
     """
     index_random = randint(0,len(list_in_which_to_choose)-1)

     return list_in_which_to_choose[index_random]

#for i in range(10):
     #print(choose_element_list([2,2,5,585,78,952,523,2355,414]))