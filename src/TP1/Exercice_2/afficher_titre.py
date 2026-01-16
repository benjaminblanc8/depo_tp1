import math


def afficher_titre(vartxt, largeur):
    if type(vartxt) is not list or type(largeur) is not int:
        return 0
    for i in vartxt:
        largeur = max(largeur, len(i)+1)
    print("*"*largeur)
    for i in vartxt:
        print("*",end="")
        print(" "*math.floor((largeur-len(i))/2-1), end="")
        print(i,end="")
        print(" "*math.floor((largeur-len(i))/2-1), end="")
        print("*")
    print("*"*largeur)

txt = ["L'ingénieux hidalgo", "Don Quichotte de la Manche", "", "Composé par Miguel de Cervantes","","Avec privilège royal","à Madrid", "en l'an de grâce 1605" ]

afficher_titre(txt, 35)
