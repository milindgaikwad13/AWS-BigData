

mydict = {'key1':'value','key2':'value2'}


print(mydict)
#{'key': 'value', 'key2': 'value2'}

print(mydict['key1'])
#value


mydict = {'key1':'value','key2':[1,2,3],'key3': {'insidekey': 100}}


print(mydict['key2'][2])
#3

print(mydict['key3']['insidekey'])
#100



mydict = {'key1':'value','key2':[1,2,3],'key3': {'insidekey': 'c'}}

print(mydict['key3']['insidekey'].upper())
#C

#Add and update
mydict['k4']= 300

print(mydict)
#{'key1': 'value', 'key2': [1, 2, 3], 'key3': {'insidekey': 'c'}, 'k4': 300}

mydict['k4']= 400

print(mydict)

#{'key1': 'value', 'key2': [1, 2, 3], 'key3': {'insidekey': 'c'}, 'k4': 400}

# list items : which are actually tuples
print(mydict.keys())
print(mydict.values())
print(mydict.items())

