class Library:
    def __init__(self, books_file="books.txt"):
        self.books_file = books_file
        self.file = open(self.books_file, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)  # Move the file pointer to the beginning
        book_lines = self.file.read().splitlines()
        if book_lines:
            for line in book_lines:
                book_info = line.split(", ")
                title, author, release_date, num_pages = book_info
                print(f"Title: {title} , Author: {author}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author: ")
        release_date = input("Enter release date: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{title}, {author}, {release_date}, {num_pages}\n"
        self.file.write(book_info)
        print(f"{title} by {author} added to the library.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        self.file.seek(0)
        book_lines = self.file.read().splitlines()

        found = False
        new_book_lines = []

        for line in book_lines:
            if title_to_remove not in line:
                new_book_lines.append(line)
            else:
                found = True

        if found:
            self.file.seek(0)
            self.file.truncate()  # Clear the file contents
            for new_line in new_book_lines:
                self.file.write(new_line + "\n")
            print(f"{title_to_remove} removed from the library.")
        else:
            print(f"{title_to_remove} not found in the library.")

lib = Library()

while True:
    print("""
    *** MENU ***
    1) List Books
    2) Add Book
    3) Remove Book
    4) Quit """)

    user_input = int(input("Enter your choice:(1-4): "))

    if user_input == 1 :
        lib.list_books()
    elif user_input == 2 :
        lib.add_book()
    elif user_input == 3 :
        lib.remove_book()
    elif user_input == 4 :
      lib.__del__()
      print("Exiting the Library Management System.")
      break
    else:
        print("Invalid choice. Please enter a valid option.")