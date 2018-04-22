class Dog:
    

    def __init__(self,name):
        self.name = name
        self.tricks = []
    def getTricks(self,trick):
        self.tricks.append(trick)
    
    
d = Dog('frodo')
e = Dog('sam')

d.getTricks('jump') 
e.getTricks('bark') 


print(d.tricks)
print(e.tricks)