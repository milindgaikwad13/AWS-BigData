


print("i'am a quoted string")

print("hello \n world \n") # new line.. escape character


#indexing

a= "hello world"

print(a)
print(a[3])

#reverse indexing

print(a[-3])






# slicing
a = "abcdefghijk"


print(a[2:])
#cdefghijk


print(a[:3])
#abc

print(a[3:6])
#def


print(a[::])
#abcdefghijk


print(a[::2]) # stepsize
#acegik


print(a[2:7:2]) #  7 is upto but not included start from 2 to 7 with stepsize 2
#ceg


print(a[::-1]) #  reverse
#kjihgfedcba



#String methods

## immutability : use concatination for change in new string

a= "sam"

# a[0] = 'P' -- error

newstr = a[1:]

print(newstr)

newstr = newstr +" test"

print(newstr *10) # dupliate the newstr 10 times

x= "Hello World"

print(x.upper())

print(x.split()) # split string based on letter, here its space into a list

print(x.split('l'))
#['He', '', 'o Wor', 'd'] it removes the split character from list



# string formatting for printing


print('This is a string {}'.format('INSERTED'))
#This is a string INSERTED
print('The {} {} {}'.format('fox','brown','quick'))
# The fox brown quick

# formatting based on position
print('The {2} {1} {0}'.format('fox','brown','quick'))
#The quick brown fox

print('The {0} {0} {0}'.format('fox','brown','quick'))
#The fox fox fox

## keyword assignemnt

print('The {q} {b} {f}'.format(f = 'fox',b = 'brown',q= 'quick'))
#The quick brown fox


## float formatting

result = 100/777

print("the result was {r}".format(r=result))
#the result was 0.1287001287001287

print("the result was {r:1.3f}".format(r=result))
#the result was 0.129


print("the result was {r:10.3f}".format(r=result)) # extra white space by adding 10
#the result was      0.129


#fstrings >= python3.6

name ="test"
print("hello, name is {}".format(name))
#hello, name is test

print(f"hello, name is {name}")
#hello, name is test


#excercise
print("{p} {r}{e}".format(p="python",r="Rules",e="!"))


mystr = 'test Data'


def myfunc(mystr):
    returnStr =''
    cnt =1
    for i in mystr:
        if( cnt%2  == 0):
            returnStr += i.upper()
        else:
            returnStr += i.lower()
        cnt +=1
    return returnStr

print(myfunc('this is a true data'))