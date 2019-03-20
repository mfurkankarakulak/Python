# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:21:17 2019

@author: furkan.karakulak
"""

# %%
#While 

i = 0
while(i<4):
    print(i)
    i=i+1

liste = [1,2,3,4,5,6,7]

uzunluk = len(liste)

each = 0
count = 0
while(each<uzunluk):
    count = count + liste[each]
    each = each +1

# %%