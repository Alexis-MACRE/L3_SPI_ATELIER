from random import randint

def gen_list_random_int(int_nbr:int=10, int_binf:int=0, int_bsup:int=10)->list:
     """Génère une liste aléatoire de int_nbr nombres compris entre int_binf et int_bsup
     
     Arguments:
     int_nbr  -- nombre de nombres aléatoires
     int_binf -- borne inférieure
     int_bsup -- borne supérieure
     
     Retourne liste_retour, la liste aléatoire
     """
     liste_retour = []

     for i in range(int_nbr):
          nbr_random = randint(int_binf,int_bsup-1)
          liste_retour += [nbr_random]

     return liste_retour

#for i in range(10):
     #gen_random_int(20,0,50)
     #print(mix_list([2,2,5,585,78,952,523,2355,414]))
     #print(choose_element_list([2,2,5,585,78,952,523,2355,414]))
     #print(extract_elements_list([2,2,5,585,78,952,523,2355,414],randint(2,10)))