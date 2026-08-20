available_books = {"Python", "Java", "C++", "DBMS", "Operating System"}
requested_books = {"Python", "DBMS", "HTML", "Java"}

available_requested = requested_books & available_books

print("Requested books that are available:")
for book in available_requested:
    print(book)