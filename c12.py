class BaseClass:
    def __init__(self):
        pass

    def add(self,a,b):
        return a + b

class Child(BaseClass):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        x =  BaseClass.add(self,self.a,self.b)
        x = x + 10
        return x

x = Child(10,10)
print x.add()