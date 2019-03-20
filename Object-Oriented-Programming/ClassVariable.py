# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:57:33 2019

@author: furkan.karakulak
"""

# %%

class employees:
    
    zam_oran = 1.8
    
    #toplam oluşturulan employee sayısını isterses bu sefer self üzerinden degil employess üzerinden işlme yapmamız gerekmektedir
    counter = 0
    
    def __init__ (self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@hotmail.com"
        
        employees.counter = employees.counter + 1

    def zam_yap(self):
        self.maas = self.maas + self.maas*self.zam_oran
        
        
calisan1 =  employees("Ahmet","Tanyeri",2000)
print("eski maas " , calisan1.maas)
calisan1.zam_yap()
print("yeni maas ",calisan1.maas)


# %%