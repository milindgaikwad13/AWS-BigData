

# 1 Use for, .split(), and if to create a Statement that will print out words that start with 's':

mystring ="Use for, .split(), and if to create a Statement that will print out words that start with 's':"




for item in mystring.split():
    if item[0].lower() == 's':
        print(item)


# 2. Use range() to print all the even numbers from 0 to 10.

for num in range(0,11,2):
    print(num)


# 3 Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.