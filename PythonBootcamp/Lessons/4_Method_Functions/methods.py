

mylist =[1,2,3,4,5]

mylist.insert(3,"test")

print(mylist)
help(mylist.insert)


def my_function(name = 'default name'):

    '''
    DOCSTRING: Information about the function
    Input: Nothing
    Output: hello

    :return:
    '''

    print("hello")
    return name

help(my_function
     )

myresult = my_function('test')
print(myresult)