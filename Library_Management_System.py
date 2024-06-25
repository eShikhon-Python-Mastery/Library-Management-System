class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} [{self.pages}]"

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if not self.is_borrowed:
            return False
        else:
            self.is_borrowed = False
            return True


class Member:

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name}  (ID: {self.member_id})"

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        else:
            return False

    def return_book(self, book):
        if book.return_book():
            self.borrowed_books.remove(book)
            return True

        return False


class Library:

    def __init__(self):
        self.members = []
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member

        return None

    def borrow_book(self, member_id, book_name):
        member = self.find_member(member_id)
        book = self.find_book(book_name)

        if member and book:
            return member.borrow_book(book)

        return False

    def return_book(self, member_id, book_name):
        member = self.find_member(member_id)
        book = self.find_book(book_name)

        if member and book:
            return member.return_book(book)

        return False

    def list_books(self):
        return self.books

    def list_members(self):
        return self.members


library = Library()

while True:
    print("Welcome to Library Management System")
    print("Please choose an option:")
    print("1. Add book")
    print("2. Add member")
    print("3. List books")
    print("4. List members")
    print("5. Borrow book")
    print("6. Return book")
    print("7. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        title = input("Enter book title: ").strip()
        author = input("Enter book author: ").strip()
        pages = input("Enter book pages: ").strip()

        book = Book(title, author, pages)
        library.add_book(book)

        print(f"Book {book.title} added to the library.")

    elif option == "2":
        name = input("Enter member name: ").strip()
        member_id = input("Enter member id: ").strip()

        member = Member(name, member_id)
        library.add_member(member)

        print(f"Member {member.name} added to the library.")

    elif option == "3":
        print(f"Books in the library:")
        for book in library.list_books():
            print(book)

    elif option == "4":
        print(f"Library members:")
        for member in library.list_members():
            print(member)

    elif option == "5":
        book_name = input("Enter book name: ").strip()
        member_id = input("Enter member id: ").strip()

        if library.borrow_book(member_id, book_name):
            print(f"Book {book_name} borrowed successfully.")
        else:
            print(f"Book {book_name} borrowed failed.")

    elif option == "6":
        book_name = input("Enter book name: ")
        member_id = input("Enter member id: ")

        if library.return_book(member_id, book_name):
            print(f"Book {book_name} returned successfully.")
        else:
            print(f"Book {book_name} returned failed.")

    elif option == "7":
        print("Thank You! Exiting the system. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
