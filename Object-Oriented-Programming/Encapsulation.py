# %%

# __ iki alttan cizgi konulursa attiribute başına private olur.
# bu private degişkenlere erişmek için get ve set methodu kullanılır.
# get ve set bir method olmayıp dünya geneleinde kabullnemiş bir isimlendirme
# private attribute degerine erişmek ve degiştirmek için bunu class içindeki functionlar ile yaparız
# methodun içi pass yazarsak methodun gövdesini boş bırakmış oluruz

## funcitonları da private yapmak için __ iki alttan çizgi koyarız içine
# bu fonskiyonlara da sadece class içinden erişebliriz


class BankAccount(object):
    
    def __init__(self,name,money,job):
        
        self.name = name
        # __money private olmuş oldu sadece class içinden erişilebilir
        self.__money = money 
        self.job = job
        
    def getMoney(self):
        return(self.__money)
    
    def setMoney(self,amount):
        self.__money =  amount
        
    # private function olmuş oldu class dışından erişilemez hale geldi    
    def __increase(self):
        self.__money = self.__money + 500
        
b1 = BankAccount("Ahmet" , 2000 , "Doktor")
b2 = BankAccount("Mehmet" , 1000 , "Eczacı")

## b1.__money bize hata verir aynı şeklide b1.__increase

print(b1.getMoney()) # bu şekilde ulaşabiliriz


# %%