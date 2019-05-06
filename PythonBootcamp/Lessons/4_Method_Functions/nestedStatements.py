

x = 25

def printer():
    x = 50
    return x

print(x)

printer()

print(x)

name = ' THIS IS THE GLOBAL'

def greet():
    name1 = 'test'

    def hello():
        print('Hello ' + name1)

    hello()
    global name

    name = "Change global"


greet()

print(name)