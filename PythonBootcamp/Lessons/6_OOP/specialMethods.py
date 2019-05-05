

class Sample():
    pass


mysample = Sample()



## specialMethods


class Book():
    def __init__(self,title, author):
        self.title = title
        self.author = author

    def __str__(self): ## this is new
        return f"{self.title} by {self.author}"

    def __len__(self):
        return 100;

    def __del__(self):
        print('A book object has been deleted')


b = Book('python','me')

print(b)
print(len(b))

del b ## delete variable from memory . this is new
b