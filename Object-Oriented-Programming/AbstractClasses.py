
# %%

# super classlar sub claslar için kullnaılacak methodları barındırır

# abstract class dan hiç bir şekilde instantiate üretilemez. Yeni nesne yaratılamaz
# bunu saglamak için bult model kullanıyoruz
# abc ==> abstract base class

# abstract mehod olması için @abstractmethod decorator alması gerek başında
#abstract class üretmek için onlarında belli bir base classden üretmek gerekiyor


from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def walk(self):
        pass
    @abstractmethod
    def run(self):
        pass
        
class Monkey(Animal):
    
    def __init__(self):
        print("Monkey")
    
    def walk(self):
        print("walk")
    
    def run(self):
        print("run")
        

m1 = Monkey()
m1.run()
m1.walk()

# %%