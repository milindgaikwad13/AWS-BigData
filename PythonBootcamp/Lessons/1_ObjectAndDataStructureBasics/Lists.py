


mylist =[1,2,3]

print(mylist)
#[1, 2, 3]

print(len(mylist))
#3

print(mylist[1:])
#[2, 3]

another_list = [4,5]
print(mylist + another_list
      )
#[1, 2, 3, 4, 5]


new_list= mylist +another_list

print(new_list)
#[1, 2, 3, 4, 5]
new_list[0] = 123
#[123, 2, 3, 4, 5]

print(new_list)


new_list.append("six")
print(new_list)
#[123, 2, 3, 4, 5, 'six']

#remove from lists
new_list.pop()
print(new_list)
#[123, 2, 3, 4, 5]

popped_item = new_list.pop() # saved poped item
print(popped_item)
#5

#[123, 2, 3, 4, 5]
popped_item = new_list.pop(2) # saved poped item pop specific location. default -1
print(popped_item)
#3

# sort
new_list= [4,1,8,5]

new_list.sort() # inplace sorting. Cant assign to another list

print(new_list)

#NoneType No value = instead of null

new_list = None

print(new_list)



