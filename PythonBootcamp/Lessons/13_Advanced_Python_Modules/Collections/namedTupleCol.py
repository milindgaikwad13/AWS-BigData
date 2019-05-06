
from collections import namedtuple



t= (1,2,4,4)

print(t)

dog =namedtuple('Dog','age breed name')

sam = dog(age=2,breed='gratedane', name='scooby')

sam.breed

