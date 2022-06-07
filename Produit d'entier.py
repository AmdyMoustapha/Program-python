# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:08:06 2022

@author: Amdy Moustapha
"""

"Produit d'entier"
def produit():
    p=1
    n1=int(input("taper n1 "))
    n2=int(input("taper n2 "))
    for i in range(n1,n2+1):
        if (n1>=1)  and (n2>=n1):
            p=p*(p+i)
    print("Le produit des entier est ",p)
print(produit())