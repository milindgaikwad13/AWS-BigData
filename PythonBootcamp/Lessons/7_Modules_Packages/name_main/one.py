
# one



def func():
    print('FUNC() in one.py')

print("Top level in one.py")

if __name__ == "__main__": # running py file directly and not as import

    print("one.py is being run directly")
else:
    print("one.py has been imported")

## write all script level functions here so that those wont get executed
#when imported
