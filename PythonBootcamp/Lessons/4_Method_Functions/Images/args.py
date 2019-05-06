

def argsfunc(*args):  # *args is a tuple
    for item in args:
        print(item)


argsfunc(1,2,4,5,6,7,8,8,"test")


def argsfunc(*spam):  # *args is a tuple
    for item in spam:
        print(item)

argsfunc(1,2,4,5,6,7,8,8,"test")


def myfunc(*args):
    return [x for x in args if x%2 == 0 ]

test = myfunc(1,2,4,5,6,67,7,8,8)
print(test)