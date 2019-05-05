

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
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')

    def bark(self):
        print('WHOOOF!!!')



my_dog = Dog()

my_dog.who_am_i()
my_dog.bark()
