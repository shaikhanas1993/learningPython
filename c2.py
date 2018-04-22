class MyClass:
    """
        A simple Class
    """

    def __init__(self,a,b):
        self.e = a
        self.f = b
    
    def hello(self):
        return self.e + self.f

x = MyClass(10,20)

print(dir(x))

print(x.hello())

x.counter = 5
while x.counter < 100:
    x.counter = x.counter * 20

print(x.counter)

del x.counter

print(id(x.hello))
print(id(MyClass.hello))