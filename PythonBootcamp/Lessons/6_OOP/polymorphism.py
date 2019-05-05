

class Animal():
    def __init__(self):
        print('ANIMAL CREATED')


    def who_am_i(self):
        print('I AM AN ANIMAL')

    def eat(self):
        print('I AM EATING')



#myanimal = Animal()
#myanimal.eat()
#myanimal.who_am_i()


class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self)

        self.name = name
        print('Dog Created')

    def bark(self):
        return 'WHOOOF!!!'

    def speak(self):
        return self.name + ' says ' + self.bark()



class Cat(Animal):
    def __init__(self,name):
        Animal.__init__(self)

        self.name = name
        print('Cat Created')

    def bark(self):
        return 'meow!!!'

    def speak(self):
        return self.name + ' says ' + self.bark()


my_dog = Dog('Scooby')

my_cat = Cat('Tom')



for pet_class in [my_dog, my_cat]:
    print(type(pet_class))
    print(pet_class.speak())



def pet_speak(pet):
    print(pet.speak())


pet_speak(my_dog)