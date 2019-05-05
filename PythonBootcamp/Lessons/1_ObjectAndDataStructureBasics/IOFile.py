

myfile =open('data/myfile.txt')

print(myfile.read())



myfile.seek(0) # seek to zero

print(myfile.read()) ## if not seek to zero then this will return empty


myfile.seek(0) # seek to zero

print(myfile.readlines()) # converts to list with each line as list entry


#close file

myfile.close()

# if file is closed the seek is not required

## new style of opening

## no need to close explicitly
with open('data/myfile.txt') as my_new_file:
    contents = my_new_file.read()
    print (contents)
    contents = my_new_file.read()
    print('read Again')
    print(contents) ## nothing printed

with open('data/myfile.txt', mode ='r')  as my_new_file:
    contents = my_new_file.read()
    print (contents)


# producing errors and not allowed

#with open('data/myfile.txt', mode ='w')  as my_new_file:
 #   contents = my_new_file.read()
 #   print (contents)

#with open('data/myfile.txt', mode='a')  as my_new_file:
 #       contents = my_new_file.read()
  #      print(contents)


## apend


with open('data/myfile.txt', mode='a')  as my_new_file:
        my_new_file.write(" this text is by python append")



with open('data/myfile.txt', mode='r')  as my_new_file:
    contents = my_new_file.read()
    print(contents)





with open('data/FileCreatedByPythonCode.txt', mode='w')  as my_new_file:
    my_new_file.write(" this text is by python create")



with open('data/FileCreatedByPythonCode.txt', mode='r')  as my_new_file:
    contents = my_new_file.read()
    print(contents)



# Reading line by line
rows =0

with open('/Users/mgaikwad/MGwork/VM_Shared/Win10Pro/Work/test2.csv', mode ='r')  as my_new_file:
    for item in my_new_file:
        print(item)
        rows += 1

print(rows)
