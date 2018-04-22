
#bad practice
def hello(self):
    print("hello ==",self)

class C:
    f = hello

    def g(self):
        return "hello world"
    
    h = g

x = C()
x.f()

    