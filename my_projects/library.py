import json
import os
from book import Book
from user import User
class Library():

    def __init__(self):
        self.books = []
        self.users = []
        self.books_file_path = os.path.join(os.path.dirname(__file__), 'library_books.json')
        self.users_file_path = os.path.join(os.path.dirname(__file__), 'users.json')
        self.load_books()
        self.load_users()
        
    def load_books(self):
        try:
            with open(self.books_file_path, 'r', encoding= 'utf-8') as f:
                self.books = json.load(f)
                self.books = [Book(**item) for item in self.books]
        except FileNotFoundError:
            self.books = []

    def load_users(self):
        try:
            with open(self.users_file_path, 'r', encoding= 'utf-8') as f:
                self.users = json.load(f)
                self.users = [User(**item) for item in self.users]
        except FileNotFoundError:
            self.users = []

    def save_books(self):
        with open(self.books_file_path, 'w', encoding = 'utf-8') as f:
            json.dump([book.__dict__ for book in self.books], f, indent=4)

    def save_users(self):
        with open(self.users_file_path, 'w', encoding = 'utf-8') as f:
            json.dump([user.__dict__ for user in self.users], f, indent=4)

    def add_book(self, title, author, isbn):
        added_book = {
            'title': title,
            'author': author,
            'isbn': isbn, 
            'copies': 1
        }
        book = Book(**added_book)
        self.books.append(book)
        self.save_books()

    def remove_book(self, isbn): 
        book = self.find_book_by_isbn(isbn= isbn)       
        if book:  
            self.books.remove(book)
            self.save_books()
        else: ValueError
        print('Sorry, we don\'t have this book')    
    
    def find_book_by_isbn(self, isbn):
        for book in self.books:
                if book.isbn == isbn:
                    return book
        return 
    
    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return
   
    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return 

    def register_user(self, user_name):
        new_id = f'{user_name[0]}{len(self.users) + 1:03d}'
        user = User(user_name, new_id)
        self.users.append(user)
        self.save_users()
        return f'User registered successfully! User ID: {new_id}'

    def borrow_book(self, user_id, isbn):
        book = self.find_book_by_isbn(isbn)
        user = self.find_user(user_id)
        if not book:
            print('Sorry, we don\'t have this book')
            return
        
        if not user:
            print('User not found')
            return
            
        if book.copies > 0:
            book.copies -= 1
            user.borrow_book(isbn) 
            print(f'{user.name} borrowed {book} successfully!')    
        else:
            print('No copies available for borrowing')                     
        self.save_books() 
        self.save_users()

    def return_book(self, user_id, isbn):
        book = self.find_book_by_isbn(isbn = isbn)
        user = self.find_user(user_id)
        if not user:
            print('User not found')
            return
        else:
            if book:
                    if book.isbn in user.borrowed_books:
                        book.copies += 1
                        user.return_book(isbn)
                        print('Book returned successfully')
                        self.save_books()
                        self.save_users()   
                    else:
                        print('You didn\'t borrow this book ')
            else: 
                print('Book not found')