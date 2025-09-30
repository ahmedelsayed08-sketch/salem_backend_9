class Animal:
    def __init__(self,name,age,species):
        self.name=name
        self.age=age
        self.species=species


    def info(self):
        print(f"name:{self.name}, age:{self.age}, species: {self.species}")

class Dog(Animal):
    def __init__(self, name, age, species,breed):
        super().__init__(name, age, species)
        self.breed=breed 

    def info(self):
        print(f"name: {self.name}, age: {self.age}, species: {self.species},breed: {self.breed}")

class Cat(Animal):
    def __init__(self, name, age, species,color):
        super().__init__(name, age, species)
        self.color=color

    def info(self):
        print(f"name: {self.name},age: {self.age},species: {self.species}, color: {self.color}")

if __name__ == "__main__":
    
    my_dog = Dog("max",1,"dog","black jack")
    my_dog.info()  

    my_cat = Cat("citte",2,"cat","orang")
    my_cat.info() 
        