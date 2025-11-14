from library import Library
my_lib = Library()
print('Welcome to My library!')

while True:
    print('  1. Show all my books:   \n'
        '  2. Register user:   \n'
        '  3. Borrow book:   \n'
        '  4. Return book:   \n'
        '  5. Exit:   ')
    choice =input("\nEnter your choice (1-5): ")
    if choice == '1':
        if not my_lib.books:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for book in my_lib.books:
                print(f"- {book.title} by {book.author} | ISBN: {book.isbn} | Copies: {book.copies}")

    elif choice == '2':
        name = input("Enter user name: ")
        print(my_lib.register_user(name))

    elif choice == '3':
        user_id = input("Enter user ID: ")
        isbn = int(input("Enter book ISBN: "))
        my_lib.borrow_book(user_id, isbn)

    elif choice == '4':
        user_id = input("Enter user ID: ")
        isbn = int(input("Enter book ISBN: "))
        my_lib.return_book(user_id, isbn)

    elif choice == '5':
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
        