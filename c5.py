class Dog:
    kind = 'canine'

    def __init__(self,name):
        self.name = name
    
    def getName(self):
        return self.name

    def getKind(self):
        return Dog.kind


dog = Dog('dog')
cat = Dog('cat')

print(dog.getName())

print(cat.getName())


print(dog.getKind())

print(cat.getKind())