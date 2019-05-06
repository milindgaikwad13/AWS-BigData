
# defaultdict


from collections import defaultdict

d ={'k1': 2}

d['k1']

d = defaultdict(object)
d['one']
for item in d:
    print (item)


d = defaultdict(lambda :0) ## create default dictionary and no error if key is missing


print(d['one'])
for item in d:
    print (item)
