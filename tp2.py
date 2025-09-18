# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:31:36 2024

@author: 33661
"""

import random         #On importe le module random

def decompose(p):     #Fonction permettant de trouver k et q
    q=p-1
    k=0
    while q%2==0:     #On décompose divise le nombre par 2 jusqu'à ce qu'il devienne un nombre impair, alors k sera le nombre de division et q le nombre impair restant
        k=k+1
        q=q/2
    return (k,int(q))


def test_decompose():    #permet de tester la fonction decompose
    if decompose(17)==(4,1) and decompose(41)==(3,5) and decompose(3)==(1,1):    #J'ai pris 4 exemple plutot simple pour m'assurer que mon programme fonctionnait
        return "La fonction decompose est ok"
    else:
        return "La fonction decompose n'est pas bonne"
    
    
def temoin_Miller_Rabin(a,p):
    (k,q)=decompose(p)      #On trouve le k et le q grâce à la fonction decompose
    b=(a**q)%p              #On applique l'algorithme pour savoir si le nombre est premier ou non.
    if b==1 or b==p-1:
        return True
    while k>0:
        b=(b**2)%p
        if b==(p-1):
            return True
        k=k-1
    return False


def Miller_Rabin(p,t):       
    for i in range(t):      #Fonction premettant de réaliser la fonction t fois avec avec t nombre aléatoire
        if temoin_Miller_Rabin(random.randint(2,p-2), p)==False:     #Si la fonction renvoie false alors le nombre n'est forcément pas premier donc on renvoie false
            return False
    return True             #Si la fonction a renvoyé t fois true alors il y a énormément de chance que le nombre soit premier (si t est grand)
       

def test_Miller_Rabin():   #Cette fonction test la fonction avec 2 nombre premier et deux nombre pas premier avec un t=40
    if Miller_Rabin(41,40)==True and Miller_Rabin(53,40)==True and Miller_Rabin(51,40)==False and Miller_Rabin(85,40)==False:
        return "La fonction Miller_Rabin est ok"
    else:
        return "La fonction Miller_Rabin n'est pas bonne"
    
    
def Miller_Rabin_40(p):  #Cette fonction utilise la liste des 40 premiers nombre premier
    nb_premier=[2,3,5,7,11,13,17,19,23,29,31,37,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173]
    vrai=0    #On fait deux variable, elles serviront a etre sur que la fonction ne fait aucune erreur.
    faux=0
    new_nb_premier=[]
    for i in range (len(nb_premier)):
        if nb_premier[i]<p:
            new_nb_premier.append(nb_premier[i])  #On ajoute tout les nombre premier avant le nombre p dans une nouvelle liste
    for i in range (len(new_nb_premier)):         #On fait un for i in range du nombre d'élément de la liste afin de tester avec tout les nombre premier possible avant le nombre p
        if temoin_Miller_Rabin(new_nb_premier[i], p)==True:
            vrai+=1
        if temoin_Miller_Rabin(new_nb_premier[i], p)==False:
            faux+=1
        if vrai!=0 and faux!=0:       #Si la fonction a renvoyer false et true pour un meme nombre p (en utilisant deux "a" différent) alors la fonction renvoie qu'elle ne marche pas bien
            return vrai, faux, "la fonction Miller_Rabin_40 n'est pas bonne"
    if vrai>0:   #Si la fonction n'a renvoyer que des true alors la variable vrai sera strictement positif, alors le nombre "p" sera premier car on aura toujours renvoyer qu'il est premier
        return True
    else: 
        return False
    
    
def Recupere_premiers(filename):     #cette fonction récupère un fichier texte
    f = open(filename, 'r')
    premiers = f.readlines()
    f.close()
    return [int(p) for p in premiers]

        
def test_primalité(p, liste_premier):   #Cette fonction test si un nombre est premier grâce a une grande liste de nombre premier
    for i in range(len(liste_premier)):
        if p==liste_premier[i]:    #Si le nombre p est dans la liste des nombres premier, alors il est lui aussi premier
            return True
        if p%liste_premier[i]==0:   #Si il est divisible par un nombre premier alors par définition il n'est pas premier
            return False
    return Miller_Rabin_40(p)   #On utilise la fonction Miller_Rabin_40 pour savoir si le nombre est premier


def test_primalité_2():   #On fait le test de la fonction précédante en utilisant le chiffre de Fermat 2**2**5 qui n'est normalement pas premier
    if test_primalité(2**(2**5), Recupere_premiers("primes_100000.txt"))==True:
        return "Le test primalité n'est pas bon"
    else:
        return "Le test primalité est ok"
    
    
def generer_premiers(n, liste_premier):   #Cette fonction permet de générer un nombre aléatoire de n bits et donne le nombre premier le plus proche
    nombre1=random.randint(1,2**n)   #On choisit un nombre aléatoire entre 1 et 2**n (pour les n bits)
    nombre2=nombre1   #Ce nombre sera afficher à la fin pour savoir quelle nombre a été choisi au départ
    if nombre1==2:    #On enlève le seuls nombre pair premier c'est à dire 2.
        return 2
    if nombre1%2==0:  #Si le nombre est pair alors on lui ajoute 1 pour qu'il soit imprair puis on lui ajoute 2 et on les test en regardant s'ils sont premier, le premier nombre premier trouvé est renvoyer par la fonction
        nombre1+=1
        while test_primalité(nombre1, liste_premier)==False:
            nombre1+=2
    if nombre1%2==1:  #Dans ce cas le nomnbre est impair alors cette fois ci on test les nombre en ajoutant 2 (tous les nombre impair) et on test s'ils sont premiers ou non.
        while test_primalité(nombre1, liste_premier)==False:
            nombre1+=2
    return nombre2, nombre1  #On retourne le nombre de départ puis le premier nombre premier qui suit
    
if _name_--'_main_':
    test_Miller_Rabin()
    test_decompose()
    test_primalité_2()
    
    
