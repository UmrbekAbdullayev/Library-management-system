# Library Management System
A small-scale Library Management System for practicing Python OOP concepts - includes book management, user handling, and JSON-based data storage.

## Features:
* Add, remove, and search books
* Register and manage users
* Borrow and return books
* Save data to JSON 

## Setup
```bash
git clone https://github.com/username/project.git
cd project
pip install -r requirements.txt
python main.py

## Usage
Run the program and follow the menu:

Welcome to the Library System!
1. Show All Books
2. Register User
3. Borrow Book
4. Return Book
5. Exit

Enter your choice: 1
Enter book title: Python Basics
Enter author: John Doe
Book added successfully!

You can:

Add a new book
Borrow a book 
Return a borrowed book
View all available books

Project Structure
library_project/
├── main.py          # Main program to run the library system
├── book.py          # Book class and related functions
├── user.py          # User class and related functions
├── data/
│   └── books.json   # Stores book information
└── README.md        # Project documentation

Contributing
Contributions are welcome! You can:
Report bugs by opening an issue
Suggest new features
Improve the code by creating a pull request
Please make sure your code is clean and well-commented.
