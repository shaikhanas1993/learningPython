

from pprint import pprint

class MyClass:
    """ a simple class example """
    i = 12345

    def __init__(self,a1,a2):
        self.a1 = a1
        self.a2 = a2
    
    def f(self):
        return 'hello world'

# print(id(MyClass())) 
x = MyClass(2,4)
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)

print(dir(x)) 