# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:04:55 2019

@author: furkan.karakulak
"""
# %%

#function tanımlanırken def ile başlar funciton ismi ve parametreler belirlendikten sonra
#bir alt satıra geçilir tab kadar boşluk olması gerekiyordur yoksa hata verir


#return etmek istersek
def myFirstFunctioninPython(var1,var2):
    """
        Buraya function ile ilgili açılamar girilebilir. Ne iş yaptıgı vs
    """
    ouput = ((var1+var2)*50.0)/(var1+var2+100) 
    
    return ouput

result = myFirstFunctioninPython(10,20)
print(result)

#return olmadan
def mySecondFunction():
    print("Bu Bir python functiondur.")

# %%