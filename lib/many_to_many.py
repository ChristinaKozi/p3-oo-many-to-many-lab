class Author:
    def __init__(self, name):
        self.name = name
        self.all = []

    def contracts(self):
        return self.all

    def books(self):
        return [contract.book for contract in self.all]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.all.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.all)


class Book:
    def __init__(self, title):
        self.title = title
        self.all = []

    def contracts(self):
        return self.all

    def authors(self):
        return [contract.author for contract in self.all]


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int) and not isinstance(royalties, float):
            raise Exception("Royalties must be a number.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.all.append(self)
        author.all.append(self)
        book.all.append(self)

    @classmethod
    def contracts_by_date(cls, target_date):
        matched_contracts = [contract for contract in cls.all if contract.date == target_date]
        sorted_contracts = sorted(matched_contracts, key=lambda contract: contract.date)
        return sorted_contracts