

## counter

# count hashbale objects


from collections import Counter

l = [1,2,4,5,3,2,3,5,5,6,2,2,4,1,4,3,5,3,2,1,6,3,2,5]

print(Counter(l))

## Counter({2: 6, 5: 5, 3: 5, 1: 3, 4: 3, 6: 2})

#dictionary of occurances


s = 'abcdfedfdsfdsaredgafdsafrefdsafdsafs'

print(Counter(s))
#Counter({'d': 8, 'f': 8, 'a': 6, 's': 6, 'e': 3, 'r': 2, 'b': 1, 'c': 1, 'g': 1})


s = " how many times word word show up in this sentense as word and wo and shoe"

print(Counter(s)) # this will give the each character count
#Counter({' ': 16, 'o': 7, 's': 7, 'w': 6, 'n': 6, 'e': 5, 'd': 5, 'h': 4, 'a': 4, 't': 3, 'i': 3, 'r': 3, 'm': 2,
# 'y': 1, 'u': 1, 'p': 1})

print(Counter(s.split())) # this will give the each word count
#Counter({'word': 3, 'and': 2, 'how': 1, 'many': 1, 'times': 1, 'show': 1, 'up': 1, 'in': 1, 'this': 1, 'sentense':
# 1, 'as': 1, 'wo': 1, 'shoe': 1})

words = s.split()


c =Counter(words)

print(c.most_common(2)) ## most common


print(sum(c.values())) ## total words in the string

print(list(c))

print(c.most_common()[:-2-1:-1])  #least common elements


