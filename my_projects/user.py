class User():

    def __init__(self, name, user_id, borrowed_books = None):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = borrowed_books if borrowed_books is not None else []
    def borrow_book(self, isbn):
        self.borrowed_books.append(isbn)

    def return_book(self, isbn):
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
                
        