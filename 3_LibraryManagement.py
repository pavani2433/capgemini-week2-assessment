class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def displaybooks(self):
        print(f'Title : {self.title}\nAuthor: {self.author}\nisbn: {self.isbn}')
        print()

booklist=[]
n=int(input("Enter number of books you need to enter "))
for i in range(n):
    title=input(f"Enter title of the book {i+1} ")
    author=input(f"Enter name of the author for book {i+1} ")
    isbn=int(input(f"Enter book isbn number for the book {i+1} "))
    book=Book(title,author,isbn)
    booklist.append(book)
for i in booklist:
    i.displaybooks()
