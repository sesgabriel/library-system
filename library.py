# The library module of the program
# I used classes, because it acts as molds to create books or users, without needing instructions all the time.
# I used the list comprehension to make the code cleaner, and more readable
import persistence

class Book:
    def __init__(self, author, title, is_loaned=False, borrowed_by=None):
        self.title = title
        self.author = author
        self.is_loaned = is_loaned
        self.borrowed_by = borrowed_by

class Library:
    def __init__(self):
        data = persistence.load_data() or {}
        self.books = [Book(b['author'], b['title'], b['is_loaned'], b['borrowed_by']) for b in data.get('books', [])]

    def save_library(self):
        data = persistence.load_data() or {}
        data['books'] = [{'title': b.title, 'author': b.author, 'is_loaned': b.is_loaned, 'borrowed_by': b.borrowed_by} for b in self.books]
        persistence.save_data(data)
    
    
    def take_books(self, title, author, user_id):
        for book in self.books:
            if (title.lower() == book.title.lower() and book.author.lower() == author.lower() and not book.is_loaned):
                book.is_loaned = True
                book.borrowed_by = user_id
                self.save_library()
                return book
        return None
    
    def find_available_book(self, title):
        available = [b for b in self.books if title.lower() == b.title.lower() and not b.is_loaned]
        return available[0] if available else None

    def return_books(self, title, author):
        for book in self.books:
            if (title.lower() == book.title.lower() and author.lower() == book.author.lower() and book.is_loaned):
                    book.is_loaned = False
                    book.borrowed_by = None
                    self.save_library()
                    return book
        return None
                
    def add_books(self, author, title):
        new_book = Book(author=author, title=title)
        self.books.append(new_book)
        self.save_library()
        return new_book
    

    def see_books(self):
        return self.books

    def find_book_by_author(self, author):
        return [b for b in self.books if author.lower() in b.author.lower()]    