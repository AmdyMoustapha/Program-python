# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:28:35 2022

@author: Amdy Moustapha
"""
"Comptage des elmts d'un tableau"

import numpy as np
def nbPairIpair():
    compt=0
    compt2=0
    
    tab = np.array([1,4,5,2,3])
    for i in range(0,5):
        if tab[i]%2==0:
            compt=compt+1
            
        else:
            compt2=compt2+1
    print("il y'a ",compt,"élément pairs ")
    print("il y'a ",compt2,"élément impairs")
print(nbPairIpair())
            