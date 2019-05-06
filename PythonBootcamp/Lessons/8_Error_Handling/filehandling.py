


try:
    f = open('testfile','w')
    f.write("write a test line")
except TypeError:
    print('the was a type error')
except OSError:
    print("os error")
finally:
    print("i always run")




try:
    f = open('testfile','r')
    f.write("write a test line")
except TypeError:
    print('the was a type error')
except OSError:
    print("os error")
except:
    print('all other errors')
finally:
    print("i always run")

## here we get os error as we opened file in read only mode and trying
# write data to file

