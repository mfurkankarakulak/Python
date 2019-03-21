

# %% 

class Website:
    
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    
    def loginInfo(self):
        print(self.name, " ",self.surname)
        
class WebSite1(Website):
    
    def __init__(self,name,surname,ids):
        Website.__init__(self,name,surname)
        self.ids = ids
        
    def Login(self):
        print(self.name, " ",self.surname,"  " , self.ids)
         
class WebSite2(Website):
    
    def __init__(self,name,surname,email):
        Website.__init__(self,name,surname)
        self.email = email
        
    def Login(self):
        print(self.name, " ",self.surname,"  " , self.email)
        

w1 = WebSite1("Ahmet","Sonuc",1)
w2= WebSite2("Mustafa Furkan","Karakulak","abc@abc")

w1.Login()
w2.Login()


# %%