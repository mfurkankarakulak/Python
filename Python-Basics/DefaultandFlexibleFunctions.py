# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:21:57 2019

@author: furkan.karakulak
"""

# user defined funciton ile built in funciton arasındaki fark bult in function python tarafından saglanan fonksiyonalardır.

# %%
#Default funciton parametrenin degeri belirlenmişse olur.
#Eger pi aşagıdaki gibi defaultuna deger verilmeseydi her seferinde bu degeride vermek gerekiyordu.
#Spesifik bir durum da bu pi degiştirmek istersek normal functionda oldugu gibi bu degeri de göndeririz
def cember_cevre_hesapla(r,pi = 3.14):
    """
        cember cevresi hesaplama
    """
    output = 2*r*pi
    return output

#Flexible funciton
#*args anlamı ister bir veya birden fazla deger veririm. İSter hiç deger vermem 
#*args -->tuble deniyor tuble kullanımı args[index] şeklinde
def flexibleFunction(var1,var2,*args):
    """
    """
    output = (var1 + var2)*args[0]
    return output

# %%