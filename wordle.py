import time
import colorama
from colorama import Fore, Back, Style
import random
colorama.init()

#avant d'avoir le fichier txt listetrie j'ai pris tous les mots du dictionnaire larousse et j'ai trié les mots qui avait 5 lettres exactement
#on lit le fichier texte, on l'enregistre dans une liste et on enregistre le nombre total de mot

filin = open("list.txt", "r")
lignes = filin.readlines()
nb_mot = len(lignes)

#on défini aléatoirement le mot choisi pour le jeu et on supprime le \n

mot_n = lignes[random.randint(0,nb_mot-1)]
mot = mot_n[0:len(mot_n)-1]

#main

print("----------")
print("| WORDLE |")
print("----------")
print("\n Vous devez trouver un mot de 5 lettres en maximum 5 essai\n")

end = 0
nb_essai = 0

while end != 1:
    saisie_utilisateur = input("Saisir le mot : ")
    if len(saisie_utilisateur) != 5:
        print("le mot saisie doit faire 5 lettres")
    else:
        if (saisie_utilisateur+"\n") in lignes:
            nb_essai += 1
            for i in range(5):
                lettre = saisie_utilisateur[i]
                if lettre == mot[i]:
                    print(Fore.GREEN + lettre, end="")
                else:
                    if lettre in mot:
                        print(Fore.YELLOW + lettre, end="")
                    else:
                        print(Fore.RED + lettre, end="")
            print(Fore.RESET)
            if saisie_utilisateur == mot:
                print("\nGagné ! le mot était", mot)
                print("Vous avez réussi en", nb_essai,"essai")
                end = 1
        else:
              print("Ce mot n'existe pas")
    if nb_essai == 5:
        print("\nPerdu ! Le mot était", mot)
        end = 1
        
time.sleep(3)
