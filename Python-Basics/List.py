# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:00:40 2019

@author: furkan.karakulak
"""

# %%
# list 
#listenin içinde hem int hem string deger olabilir
#liste tanımı type' ı listdir
liste = [1,2,3,4,5,6]

liste_str = ["pts","sl","crsmb","prsmb","cuma"]

# listin içinde elaman almak istersen index mantıgı vardır.
var = liste_str[2]

#liste son eleman 
lastVar = liste[-1]

#belli bir yerden başlayıp şu kadar eleman getir dersen
# 0. indexden başa 0,1,2 ye kadar getir demek
list_divide =  liste[0:3]

#list type içerinde kullanılabilecek methodları görmek için
#dir(list) kullanılır
usableFunciton = dir(list)

# bir method hakkında bilgi almak için
#mesela apend listenin sonuna eleman eklermiş consoleda gördük bunu 
helpMethod = help(list.append)

# %%