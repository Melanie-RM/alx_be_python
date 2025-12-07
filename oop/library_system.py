from library_system import Book,Ebook,PrintBook, Library

def main():
    library = Library()

    book1 = book("The Alchemist","Paulo Coelho")
    ebook1 = Ebook("Digital Fortress","Dan Brown",5)
    printbook1 = PrintBook("1984","George Orwell",328)

    library.add_book(book1)
    library.add_book(ebook1)
    library.add_book(printbook1)

if __name__ == "__main__":
    main()