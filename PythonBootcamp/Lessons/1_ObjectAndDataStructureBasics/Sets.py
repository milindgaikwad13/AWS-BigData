

myset = set()

myset.add(1)

print(myset)
# {1}

myset.add(2)
print(myset)
# {1, 2}


myset.add(2) # unique values
print(myset)
# {1, 2}


## remove duplicates from list( convert to set )


a = [1,1,1,1,1,1,2,2,2,2,1,1,1,4,6,3,2]

print(a)
#[1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 4, 6, 3, 2]
print(set(a))

#{1, 2, 3, 4, 6}

b =list(set(a))
print(b)
# [1, 2, 3, 4, 6]


# excercise:

# print unique characters from word Mississippi with one line code
print(set(list('Mississippi')))

# {'i', 'M', 's', 'p'}