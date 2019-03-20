# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:33:16 2019

@author: furkan.karakulak
"""
# %%

var1 = 10
var2 = 20

if(var1 > var2):
    print("var1 büyüktür var2")
elif(var1 == var2):
    print("var1 == var2")
else:
    print("var1 kücüktür var2")

#bir degerin liste içinde olup olamdıgını kontrol etmke için aşagıdaki şekilde kullnaılır
liste = [1,2,3,4,5,6]

value = 0

if value in liste:
    print("evet {} degeri listede var".format(value))
else:
    print("hayir")


# %%