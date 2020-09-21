# Auteur(s) : MACRE Alexis
# Date : 21/09/2020
# Version : 4.0
# Description : Fonction de test


def test_fonction(fonction:callable,valeurs:list,valeurs_attendues:list,affichage_variable:bool=True) -> None :
     """Fonction qui permet de tester une fonction pour chacune des valeurs passées en paramètre.
     Elle compare les valeurs que la fonction retourne à celles qui sont attendues, puis affiche les résultats du test.
     Possibilité de désactiver l'affichage des valeurs d'entrées, dans le cas par exemple où cette dernière est très 
     volumineuse (comme une liste de 15000 mots)
     
     Arguments:
     fonction            -- la fonction à tester
     valeurs             -- liste des paramètres en entrée pour chacun des tests
     valeurs_attendues   -- liste des valeurs de retour attendues
     affichage           -- affichage ou non de la valeur en entrée
     """

     for i in range(len(valeurs)):                                              

          resultat = fonction(*valeurs[i]) 

          if affichage_variable:
               val_affiche = "pour " + str(valeurs[i])
          else:
               val_affiche = "numero " + str(i)

          if resultat!=valeurs_attendues[i]:
               print("Test",val_affiche,": Resultat Incorrect",resultat,"au lieu de",valeurs_attendues[i])
          else:
               print("Test",val_affiche,": Resultat Correct",resultat)




# import sys
# sys.path.append('../L3')
# import testfonction