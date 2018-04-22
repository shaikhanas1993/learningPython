class MyClass:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def hello(self):
        return "hello world!"

    def add(self):
        return self.a + self.b

x = MyClass(10,10)

print(x.add())

x.counter = 10
while x.counter<100:
    x.counter = x.counter* 20

print(x.counter)




print(dir(x))