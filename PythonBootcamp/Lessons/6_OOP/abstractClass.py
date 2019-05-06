

## polymorphism


class Animal():
    def __init__(self, name):
        self.name = name
        print('ANIMAL CREATED')

    def speak(self):
        raise  NotImplementedError(" Subclass must implement this abstract method")



class Dog(Animal):

    def speak(self):
        return self.name + " Says Wooof!!!"


class Cat(Animal):

    def speak(self):
        return self.name + " Says meow!!!"


scooby = Dog('Scooby')

tom = Cat('Tom')


print(scooby.speak())
print(tom.speak())



