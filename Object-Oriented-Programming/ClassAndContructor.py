# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:42:01 2019

@author: furkan.karakulak
"""

# %% 

class calisan:
    
    #contructor 
    def __init__ (self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim +"@hotmail.com"
    
    def giveNameAndSurname(self):
        return "isim " + self.isim +" soyisim " +self.soyisim
        

isci1 = calisan("MsutafaFurkan","Karakulak",10000)

print(isci1.giveNameAndSurname())

# %% 