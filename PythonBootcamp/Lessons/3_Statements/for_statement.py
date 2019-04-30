

  # for

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for jelly in mylist:
    print(jelly)


string = "my test string"

for s in string:
    print(s)

for _ in string:
    print('not using string characters')


t= (1,2,3)

for t1 in t:
    print(t1)

mylist =[(1,2),(3,4),(5,6),(7,8)]

print(len(mylist))

for item in mylist:
    print(item)

# tuple unpacking

for a,b in mylist:
    print(a)
    #print(b)

# dictionaries

d = {'key':1,'key2':2,'key3':"test"}

for key,value in d.items():
    print(key)
    print(value)