import pytest
from book_dao import BookDAO
from book import Book

class Test_Book:
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.book_dao = BookDAO(db_file="database.db")

        self.book1 = Book(title="bok1", description="Beskrivning1", author="Författare1")
        self.book2 = Book(title="bok2", description="Beskrivning2", author="Författare2")
        self.book3 = Book(title="bok3", description="Beskrivning3", author="Författare3")

        self.book_dao.insert_book(self.book1)
        self.book_dao.insert_book(self.book2)
        self.book_dao.insert_book(self.book3)
        yield
        self.book_dao.clear_table()
        self.book_dao.close()

    def test_get_all_book(self):
        books = self.book_dao.get_all_books()
        print(books)
        assert len(books) == 3
        
    def test_add_book(self):
        new_book = Book(title="bok4", description="Beskrivning4", author="Författare4")
        self.book_dao.insert_book(new_book)
        books = self.book_dao.get_all_books()
        assert len(books) == 4

    def test_get_description(self):
        book = self.book_dao.find_by_title("bok1")
        assert book.description == "Beskrivning1"

    def test_get_book_from_title(self):
        book = self.book_dao.find_by_title("bok1")
        book.description = "Ny beskrivning"
        self.book_dao.update_book(book)
        assert book.description == "Ny beskrivning"

    def test_delete_book(self):
        book = self.book_dao.find_by_title("bok1")
        self.book_dao.delete_book(book)
        assert self.book_dao.find_by_title("bok1") == None