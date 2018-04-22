# class BaseClass:
#     def __init__(self):
#         self.default = 0
    
#     def getDefault(self):
#         return self.default


# class Derived(BaseClass):
#     def __init__(self):
#         print dir(self)
#         self.default = 5
    

# x = Derived()
# # print dir(x)

# print x.getDefault()

class BaseClass:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b

class Derived(BaseClass):
    def __init__(self):
        pass
    
# y = BaseClass(5,10)    
x = Derived()
x.a = 10
x.b = 20
print x.add()


