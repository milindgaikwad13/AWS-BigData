
### map

def square(num):
    return num**2

print(square(3))


my_nums = [1,2,3,4,5]

for item in map(square,my_nums):
    print(item)

mylst =  list(map(square, my_nums))

print(mylst)



def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'Even'
    else:
        return mystring[0]

names = ['test','pqr','xyz']

print(list(map(splicer,names)))



# filter

def check_even(num):
    return num%2 == 0


mynums =[1,2,3,4,5,6]

print(list(filter(check_even,mynums)))


# lambda

print(list(map(lambda num: num**2 , mynums)))
print(list(filter(lambda num: num%2==1 , mynums)))