# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 14:13:47 2022

@author: Amdy Moustapha
"""

"exercice 12"

def tri(t):
    for i in range(0,len(t)-1):
        min=t[i]
        ind=i
        for j in range(i+1,len(t)):
            if t[j]<min:
                min=t[j]
                ind=j
        tp=t[i]
        t[i]=t[ind]
        t[ind]=tp
        
            
import random
tab = [random.randint(0,100) for i in range(10)]
print(tab)
tri(tab)
print(tab[0],",",tab[1],",",tab[2],",",tab[3],",",tab[4],",",tab[5],",",tab[6],",",tab[7],",",tab[8],",",tab[9])
