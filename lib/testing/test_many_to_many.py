from lib.many_to_many import Author, Book, Contract

def test_contract_initializes():
    author = Author("Author One")
    book = Book("Book One")
    contract = Contract(author, book, "2024-01-01", 1000)
    assert contract.author == author
    assert contract.book == book
    assert contract.date == "2024-01-01"
    assert contract.royalties == 1000

def test_author_contracts():
    author = Author("Author A")
    book = Book("Book A")
    Contract(author, book, "2024-01-02", 500)
    assert len(author.contracts()) == 1

def test_author_books():
    author = Author("Author B")
    book1 = Book("Book B1")
    book2 = Book("Book B2")
    Contract(author, book1, "2024-01-03", 300)
    Contract(author, book2, "2024-01-04", 400)
    assert len(author.books()) == 2

def test_book_contracts():
    author = Author("Author C")
    book = Book("Book C")
    Contract(author, book, "2024-01-05", 600)
    assert len(book.contracts()) == 1

def test_book_authors():
    author = Author("Author D")
    book = Book("Book D")
    Contract(author, book, "2024-01-06", 800)
    assert len(book.authors()) == 1

def test_sign_contract():
    author = Author("Author E")
    book = Book("Book E")
    contract = author.sign_contract(book, "2024-01-07", 700)
    assert isinstance(contract, Contract)

def test_total_royalties():
    author = Author("Author F")
    book = Book("Book F")
    Contract(author, book, "2024-01-08", 400)
    Contract(author, book, "2024-01-09", 600)
    assert author.total_royalties() == 1000

def test_contracts_by_date():
    author = Author("Author G")
    book = Book("Book G")
    Contract(author, book, "2024-01-10", 100)
    Contract(author, book, "2024-01-11", 200)
    contracts = Contract.contracts_by_date("2024-01-10")
    assert len(contracts) == 1
    assert contracts[0].date == "2024-01-10"