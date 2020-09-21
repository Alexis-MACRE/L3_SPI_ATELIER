# Auteur(s) : 
# Date : xx/xx/2020
# Version : 1.0
# Description : Atelier de programmation x Exo x Python

def fill_list(b_inf:int,b_sup:int,max_len:int)->list:
     """Demande à l'utilisateur de rentrer des entiers compris entre les 2 bornes un à un qui sont ensuite stocké dans une liste
     de longueur maximum max_len. 
     La fonction s'arrête si l'utilise rentre une valeur incorrecte (non entière, ou non comprise dans les bornes)

     Arguments:
     b_inf -- borne inférieure
     b_sup -- borne suppérieure
     max_len -- longueur maximale de la liste

     Retourne la liste des entrées
     """
     saisie_incorrecte = False
     i = 0
     liste_retour = []

     while (not saisie_incorrecte) and i < max_len:

          saisie = input("Veiller rentrer l'élement de la liste: ")

          if saisie.isdigit():
               entier_saisie = int(saisie)

               if b_inf<=entier_saisie<=b_sup:
                    liste_retour.append(entier_saisie)
                    i +=1
               else:
                    saisie_incorrecte = True
                    print("Vous avez rentré une valeur en dehors des bornes")
          else:
               saisie_incorrecte = True
               print("Vous n'avez pas rentré un entier")
          
     return liste_retour


def test_fill_list(fonction_fill:callable,valeurs:list,valeurs_attendues:list):
     """Fonction de test pour la fonction fill. Affiche le resultat du test

     Arguments:
     fonction_fill     -- la fonction fill à tester
     valeurs           -- la liste de valeurs avec lesquelles vous souhaitez tester la fonction
     valeurs_attendues -- la liste des valeurs attendues en retour
     """
     for i in range(len(valeurs)):

          resultat = fonction_fill(valeurs[i][0],valeurs[i][1],valeurs[i][2])

          if resultat == valeurs_attendues[i]:
               print("Test réussi pour la valeur",valeurs[i],"la fonction a bien retourné ",valeurs_attendues[i])
          else:
               print("Test échoué pour la valeur",valeurs[i],"valeur retournée:",resultat)


test_fill_list(fill_list,  [[1,10,3],[1,10,8],[0,0,5],[0,0,0]]   ,  [[1,1,1],[2,2,2,2,2,2,2,2],[],[]]  )


