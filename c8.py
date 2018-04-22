counter = 1

class Bag:
    def __init__(self):
        self.data = []
    def add(self,x):
        self.data.append(x)
    
    def addTwice(self,x):
        self.add(x)
        self.add(x)
        global counter 
        counter = counter + 2


x = Bag()
x.addTwice(4)
print x.data

print counter


print counter.__class__
print type(4)