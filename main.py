import traceback
import numpy as np

# Define a class to represent a book with title, author, and availability status
class book:
    def __init__(self, title, author, availability):
        # Initialize the attributes of the book
        self.title = title
        self.author = author
        self.availability = availability

    def display(self):
        # Method to display the book's details (title, author, and availability)
        print("the title : ", self.title, "\nthe author : ", self.author)
        print("the availability: ", self.availability)

    def availability_update(self, update):
        # Method to update the availability status of the book
        self.availability = update

# Define a class to represent a library that contains a list of books
class library:
    def __init__(self):
        # Initialize the library with a single default book
        self.lists = [book("big one", "refaat", False)]  # Example book with False availability

    def display(self):
        # Method to display all books in the library
        if len(self.lists) >= 1:
            for book_instance in self.lists:
                # For each book in the library, display its details
                book_instance.display()

    def add_book(self, title, author, availability):
        # Method to add a new book to the library
        self.lists.append(book(title, author, availability))

    def book_availability_updata(self, title, update):
        # Method to update the availability of a book by title
        for i in self.lists:
            if i.title == title:
                # If the book with the given title is found, update its availability
                i.availability_update(update)

# Define an exception handling function to catch and handle specific exceptions
def exception_handling(ex):
    # Handle different types of exceptions and restart the program if an error occurs
    if isinstance(ex, FileNotFoundError):
        print("please make sure you have a file to save")
        main_program()
    elif isinstance(ex, PermissionError):
        print("please make sure you have permission to open and write in this file")
        main_program()
    elif isinstance(ex, IndexError):
        print("please make sure you chose a correct line index")
        main_program()
    elif isinstance(ex, ValueError):
        print("please make sure you enter an integer number as a choice")
        main_program()
    else:
        # Default case for any unhandled exception
        main_program()

# Main function where the user interacts with the library system
def main_program():
    try:
        # Create a new library instance
        lib = library()

        while True:
            # Display menu options to the user
            print("please enter the option:\n1-display books \n2-add book")
            user_in = int(input("3- update availability\nyour choice : "))

            # Use match-case to handle different user choices
            match user_in:
                case 1:
                    # Option 1: Display all books in the library
                    lib.display()
                case 2:
                    # Option 2: Add a new book to the library
                    title = input("please enter the book title  : ")
                    author = input("enter the author:  ")
                    availability = bool(input("enter the availability (True or False):  "))  # Convert input to bool
                    lib.add_book(title, author, availability)
                case 3:
                    # Option 3: Update the availability of a book
                    title = input("please enter the book title: ")
                    availability = bool(input("please enter the availability (True or False):  "))  # Convert input to bool
                    lib.book_availability_updata(title, availability)
                case _:
                    # If the user enters an invalid option, print a message
                    print("please enter a valid choice")
    except Exception:
        # If an exception occurs, handle it by calling exception_handling
        exception_handling(Exception)

# Start the program
main_program()
