# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:26:40 2024

@author: 33661
"""

#COCHARD Mathieu 1A Info TP3
from math import sqrt
from math import ceil
from sympy import randprime

def FactorisationNaive(N):
    p=ceil(sqrt(N))
    iteration=0
    while N%p != 0:
        p+=1
        iteration+=1
    q= N//p
    return p, q, iteration


def test_FactorisationNaive(): #Test avec valeur 47941
    if FactorisationNaive(47941)==(251, 191, 251 - ceil(sqrt(47941))):
        print ("fonction FactorisationNaive et nombres iterations: ok")
    else:
        print ("fonction FactorisationNaive et nombre iteration : pas ok")



def estCarre(x): #Savoir si x est un carre
    z=int(sqrt(x))
    if z**2 == x:
        return True
    else:
        return False
    
    
def test_estCarre():
    if estCarre(25)==True and estCarre(36)==True and estCarre(45)==False and estCarre(62)==False:
        print("fonction estCarre : ok")
    else:
        print("focntion estCarre : pas ok")
        
        
def Fermat(N):  
    x=ceil(sqrt(N))
    iteration = 0
    while estCarre(x**2-N)==False:
        x+=1
        iteration += 1
    p=x+sqrt(x**2-N)
    q=x-sqrt(x**2-N)
    return (int(p),int(q), iteration)


def test_Fermat():
    if Fermat(47941)==(251,191,((251+191)/2)-ceil(sqrt(47941))):
        print ("fonction Fermat et nombre iterations : ok")
    else:
        print ("fonction Fermat et nombre iterations : pas ok")
        

def test_Complexite():
    n=16
    p = randprime(1 << (n-1), (1 << n)-1)
    q = randprime(1 << (n-1), (1 << n)-1)
    
    N=p*q
    if Fermat(N)[2]==(p+q)//2-ceil(sqrt(N)) and FactorisationNaive(N)[2]==max(p,q)-ceil(sqrt(N)):
        print ("fonction testComplexite : ok")
    else:
        print ("fonction testComplexite : pas ok")
    

if __name__=='__main__':
    test_Fermat()
    test_Complexite()
    test_estCarre()
    test_FactorisationNaive()
    
