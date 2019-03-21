# %%

class Employee:
    
    def Raise(self):
        raise_rate = 0.1
        result = 100 + 100*raise_rate
        print("Employee " , result)
        
class ComEng(Employee):
    
    def Raise(self):
        raise_rate = 0.2
        result = 100 + 100*raise_rate
        print("ComEng " , result)
        
class EEE(Employee):
    
    def Raise(self):
        raise_rate = 0.3
        result = 100 + 100*raise_rate
        print("EEE " , result)
        
e1 = Employee()
c1 = ComEng()
eee1 = EEE()

object_list = [e1,c1,eee1]

for item in object_list:
    item.Raise()


# %%