class Dog:
    def __init__(self,name,breed,age,color):
        self.name =name
        self.breed =breed
        self.age =age
        self.color =color

    def sound(self):
        print(self.name,"is barking")


dog1 =Dog("Victory","German Shepherd",5,"white")
print(dog1.name)

dog2= Dog("Braxton","Siberian Husky",2,"brown")
print(dog2.breed,dog2.age,dog2.color)
dog2.sound()


dog3 =Dog("Abigael","Chihuahua",5,"Black")
print(dog3.color)