# %%

class Calculator(object):
    
    def __init__(self,value1,value2):
        
        #attribute
        self.value1 = value1
        self.value2 = value2
        
    def add(self):
        return(self.value1 + self.value2)
        
    def multiply(self):
        return(self.value1 * self.value2)
        
    def subtraction(self):
        return(self.value1 - self.value2)
        
    def divide(self):
        return(self.value1 / self.value2)


print("Please Choose Operation")
print("ADD 1")
print("MULTIPLY 2")
print("SUBTRACTION 3")
print("DIVIDE 4")

selection = input()
print("First value ")
firstValue = int(input())
print("Second value ")
secondValue = int(input())

c1 = Calculator(firstValue,secondValue)


if selection == "1":
    print(c1.add())
elif selection == "2":
    print(c1.multiply())
elif selection == "3":
    print(c1.subtraction())    
elif selection == "4":
    print(c1.divide())


# %%