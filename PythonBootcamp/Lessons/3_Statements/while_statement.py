


x= 50
while x <5:
    print (f'current value of x is {x}')
    x += 1

else :
    print('x is not less than 5')

x= [1,2,3]

for _ in x:
    pass # do nothing .. this is new


# continue

mystring = "test123"
for x in mystring:
    if x == '1':
        continue
    if x == '2':
        break
    print(x)

x = 0

while x<5:
    print(x)
    break