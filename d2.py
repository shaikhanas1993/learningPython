class Base:
    def __init__(self,iterable):
        self.myList = []
        self.__update(iterable)
    
    def update(self,iterable):
        for item in iterable:
            self.myList.append(item)

    __update = update

class Child(Base):
    def update(self,keys,values):
        for item in zip(keys,values):
            self.myList.append(item)



x = Child([1,2])
print x.myList

x.update((1,2),(3,4))
print x.myList