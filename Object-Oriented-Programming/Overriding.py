# %%

class Animal: # parent
    
    def toString(self):
        print("Animal")
        
class Bird(Animal): # child inherit aldık
    
    def toString(self): #Override ettik
        print("Bird")
        

a1 = Animal()
a1.toString()

b1 = Bird()     
b1.toString()

Ü# %%