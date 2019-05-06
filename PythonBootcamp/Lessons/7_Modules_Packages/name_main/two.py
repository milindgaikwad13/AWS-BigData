import one


print ("Top level in two.py")

one.func()


if __name__ == "__main__":
    print ("tow.py is being run directly")
else:
    print( "tow .py is imported ")