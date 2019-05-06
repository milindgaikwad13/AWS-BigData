

class NameOfClass():

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2


    def some_method(self):
        print(self.param1)



obj = NameOfClass(1,2)

obj.some_method()



class Dog():

    def __init__(self, breed):
        self.breed = breed

    
my_dog = Dog(breed="Lab")

my_dog.breed


my_dog.breed= "test"

print(my_dog.breed)










