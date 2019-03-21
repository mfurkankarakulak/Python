# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# %%
# class
    
class Emp(object):
    
    age = 25
    salary = 4000
    
    def ageSalaryRatio(self):
        print(self.salary/self.age)

e1 = Emp()
e1.ageSalaryRatio()

#method

def ageSalaryRatio  (age,salary):
    print("function : " , salary/age)
    
ageSalaryRatio(25,4000)


# %%
# class constructor or initializer

class Animal(object):
    
    def __init__(self,age,name):
        self.age = age
        self.name = name
        
a1 = Animal(24,"Ali")



#%%