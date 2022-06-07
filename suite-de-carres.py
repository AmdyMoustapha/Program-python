# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 13:34:03 2022

@author: Amdy Moustapha
"""

"Suite de carrés"
def affichercarre():
    n=int(input("n="))
    liste_carres=[]
    for i in range(n+1):
        carre = i*i
        liste_carres.append(carre)
    return liste_carres
print(affichercarre())