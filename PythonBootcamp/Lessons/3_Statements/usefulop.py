

# Range



for x in range(1,20): # last is not included
    print(x)


word = 'abcd'

for item in enumerate(word):
    print(item)

    #(0, 'a')
    #(1, 'b')
    #(2, 'c')
    #(3, 'd')

for index,letter in enumerate(word):
    print(index)


#zip

mylist1 =[1,2,3,4,5,6]
mylist2 = ['a','b','c']

zip(mylist1,mylist2) ## zipper on a jacket

for item in zip(mylist1,mylist2): ## inner join ( exludes if uneven count).. shortest list is shown
    print(item)

if 2 in mylist1:
    print('true')


from random import shuffle

print(mylist1)


from random import randint

print(randint(0,100))


st = None

st = input("input st:") ## always stores as string
print(st)