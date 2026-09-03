books = {}


def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")

    books[book_id] = {
        "title": title,
        "author": author,
        "available": True
    }


def search_book():
    book_id = input("Enter book ID: ")

    if book_id in books:
        print(books[book_id])
    else:
        print("Book not found")


def issue_book():
    book_id = input("Enter book ID: ")

    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        print("Book issued")
    else:
        print("Book not available")


def return_book():
    book_id = input("Enter book ID: ")

    if book_id in books:
        books[book_id]["available"] = True
        print("Book returned")


def display_available():
    for book_id, book in books.items():
        if book["available"]:
            print(book_id, book)


add_book()
display_available()