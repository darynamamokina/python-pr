import random

class Page:
    def __init__(self, page_number, content, image_url=None):
        self.page_number = page_number
        self.content = content
        self.image_url = image_url

class Book:
    def __init__(self):
        self.pages = []  # Масив сторінок книги
        self.format = None  # Формат книги (наприклад, PDF, ePub)

    def set_format(self, book_format):
        self.format = book_format

    def add_page(self, page):
        self.pages.append(page)

    def get_contents(self):
        return self.pages

class BookBuilderBase:
    def __init__(self):
        self.book = None

    def add_page(self, page):
        raise NotImplementedError("Subclasses must implement add_page method")

    def set_format(self, book_format):
        self.book.set_format(book_format)

    def get_book(self):
        return self.book

class ScientificBookBuilder(BookBuilderBase):
    def __init__(self):
        super().__init__()
        self.book = Book()
        self.book.format = "PDF"

    def add_page(self, page_number, content, image_url=None):
        page = Page(page_number, content, image_url)
        self.book.add_page(page)

class NovelBookBuilder(BookBuilderBase):
    def __init__(self):
        super().__init__()
        self.book = Book()
        self.book.format = "ePub"

    def add_page(self, page_number, content, image_url=None):
        page = Page(page_number, content, image_url)
        self.book.add_page(page)

class ManualBookBuilder(BookBuilderBase):
    def __init__(self):
        super().__init__()
        self.book = Book()
        self.book.format = "PDF"

    def add_page(self, page_number, content, image_url=None):
        page = Page(page_number, content, image_url)
        self.book.add_page(page)

# Створення книги наукового типу
scientific_book_builder = ScientificBookBuilder()
scientific_book_builder.add_page(1, "Сторінка 1: Вступ", "https://i.insider.com/602ee9d81a89f20019a377c6?width=1136&format=jpeg")
scientific_book_builder.add_page(2, "Сторінка 2: Розділ 1", "https://example.com/image2.jpg")
scientific_book = scientific_book_builder.get_book()

# Створення книги белетристики
novel_book_builder = NovelBookBuilder()
novel_book_builder.add_page(1, "Сторінка 1: Перший розділ", "https://example.com/image3.jpg")
novel_book_builder.add_page(2, "Сторінка 2: Другий розділ", "https://example.com/image4.jpg")
novel_book = novel_book_builder.get_book()

# Створення посібника
manual_book_builder = ManualBookBuilder()
manual_book_builder.add_page(1, "Сторінка 1: Інструкція", "https://example.com/image5.jpg")
manual_book_builder.add_page(2, "Сторінка 2: Додаток", "https://example.com/image6.jpg")
manual_book = manual_book_builder.get_book()

# Отримання вмісту книг
for page in scientific_book.get_contents():
    print(f"Page {page.page_number}: {page.content}, Image URL: {page.image_url}")

for page in novel_book.get_contents():
    print(f"Page {page.page_number}: {page.content}, Image URL: {page.image_url}")

for page in manual_book.get_contents():
    print(f"Page {page.page_number}: {page.content}, Image URL: {page.image_url}")
