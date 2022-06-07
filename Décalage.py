# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:29:39 2022

@author: Amdy Moustapha
"""
"Décalage"
import numpy as np
def decaleCircdriote():
    tableau = np.array([1,2,4,5,6])
    newtableau= np.roll(tableau,1)
    return newtableau
print(decaleCircdriote())