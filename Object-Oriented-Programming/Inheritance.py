

# %%

class Animal(object):
    
    def __init__(self):
        print("Animal is created")
        
    def walk(self):
        print("Animal is walking")
    
    def toString(self):
        print("Animal")

class Monkey(Animal):
    
    def __init__(self):
        super().__init__() #base classın constructorunu çagırma
        print("Monkey is created")
    
    def toString(self):
        print("Monkey")
    
    def Climb(self):
        print("Monkey is climbing")
        
    
class Bird(Animal):
    
    def __init__(self):
        super().__init__()
        print("Bird is created")
        
    def toString(self):
        print("Bird")
        
    def fly(self):
        print("bird is flying")
        

m1 = Monkey()
m1.Climb()
m1.toString() 
m1.walk() ## bu funtion base classdan geldi

print("----------")

b1 = Bird()
b1.fly()
b1.toString()
b1.walk()

# %%