class Base:
    def __init__(self):
        pass
    
    def add(self,a,b):
        return a + b


class Derived(Base):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        return Base.add(self,self.a,self.b)

x = Derived(10,20)
print x.add()

print isinstance(x,Derived)

print isinstance(x,Base)

print issubclass(Derived,Base)

print issubclass(Base,Derived)