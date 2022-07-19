class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type},weighting {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight+100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


book = Book("Harry Potter", "Hardcover", 1500)
print(Book.TYPES)

book2 = Book("Dehui", "Paperback", 2)


def store_details(store):
    return f'{store.name}, total stack price:{store.stock.price()}'
