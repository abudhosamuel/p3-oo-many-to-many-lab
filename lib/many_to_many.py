class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self._contracts = []  # Storage for contracts
        Author.all_authors.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        self._contracts.append(new_contract)
        book.contracts.append(new_contract)  # Ensure the book also tracks this contract
        return new_contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    all_books = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string.")
        self.title = title
        self.contracts = []  # Add this to track contracts related to this book
        Book.all_books.append(self)

    def contracts(self):
        return self.contracts

    def authors(self):
        return list(set([contract.author for contract in self.contracts]))



class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author) or not isinstance(book, Book):
            raise Exception("Author must be an Author and book must be a Book.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]
