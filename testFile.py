from Book import Book
from BookCollectionNode import BookCollectionNode
from BookCollection import BookCollection
def test_Book():
    b0 = Book("Cujo","King, Stephen",1936)
    b1 = Book("19","King, Stephen",1977)
    assert b0.getAuthor() == "King, Stephen"
    assert b1.getTitle() == "The Shining"
    assert b0.getBookDetails() == "Title: Cujo, Author: King, Stephen, Year: 181"
    assert b1.getYear() == 1977

    
def test_BookCollection():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc = BookCollection()
    assert bc.isEmpty() == True
    bc.insertBook(b0)
    bc.insertBook(b1)
    assert bc.getNumberOfBooks() == 2
    assert bc.isEmpty() == False
    bc.insertBook(b3)
    assert bc.getBooksByAuthor("King, Stephen") == "Title: Cujo, Author: King, Stephen, Year: 1981\nTitle: The Shining, Author: King, Stephen Year: 1977\nTitle: Rage, Author: King, Stephen, Year:1977\n"
    assert bc.getNumberOfBooks() == 3
    assert bc.getAllBooksInCollection() == "Title: Cujo, Author: King, Stephen, Year: 1981\nTitle: The Shining, Author: King,Stephen, Year: 1977\nTitle: Ready Player One, Author: Cline, Ernest Year: 2011\nTitle: Rage, Author: King, Stephen, Year: 1977\n"

def test_BookCollectionNode():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    n = BookCollectionNode(b0)
    assert n.getData() == b0
    n.setNext(b1)
    assert n.getNext() == b1
    n2 = BookCollectionNode(b3)
    assert n2.getData() == b3

    
    
