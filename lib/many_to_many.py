from datetime import datetime

class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [c for c in Contract.all if c.author == self]

    def books(self):
        return list(set([c.book for c in self.contracts()]))

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([c.royalties for c in self.contracts()])


class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        return list(set([c.author for c in self.contracts()]))


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be of type Author")
        if not isinstance(book, Book):
            raise Exception("Book must be of type Book")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not self.valid_date_format(date):
            raise Exception("Date must be in YYYY-MM-DD format")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        if not cls.valid_date_format(date):
            raise Exception("Date must be in YYYY-MM-DD format")
        return [c for c in sorted(cls.all, key=lambda c: c.date) if c.date == date]

    @staticmethod
    def valid_date_format(date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False