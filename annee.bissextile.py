# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 13:02:48 2022

@author: Amdy Moustapha
"""

"année bissextile"

annee= int(input("choisir une année"))

if(annee%4==0 and annee%100!=0) or annee%400==0: 
    print("bissextile")
else:
    print("non bissextile")