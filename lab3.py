import random

#id сторінок
class PageRegistry:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.pages = {}
        return cls._instance

    def generate_unique_id(self):
        unique_id = random.randint(1, 10000)
        while unique_id in self.pages:
            unique_id = random.randint(1, 10000)
        return unique_id

    def register_page(self, page):
        page_id = self.generate_unique_id()
        self.pages[page_id] = page
        return page_id

class Page:
    def __init__(self, page_number, content, image_url=None, references=None, glossary=None, characters=None):
        self.page_number = page_number
        self.content = content
        self.image_url = image_url
        self.references = references if references is not None else []
        self.glossary = glossary if glossary is not None else []
        self.characters = characters if characters is not None else []

    def add_reference(self, reference):
        self.references.append(reference)

    def add_to_glossary(self, term, definition):
        self.glossary.append((term, definition))

    def add_character(self, name, description):
        self.characters.append((name, description))

class Book:
    def __init__(self, title):
        self.pages = []  # Масив сторінок книги
        self.format = None  
        self.title = title
        self.characters = [] 

    def set_format(self, book_format):
        self.format = book_format

    def add_page(self, page):
        self.pages.append(page)

    def get_contents(self):
        return self.pages

    def add_character(self, name, description):
        self.characters.append((name, description))

    def __str__(self):
        total_pages = len(self.pages)
        return f"Title: {self.title}\nFormat: {self.format}\nTotal Pages: {total_pages}"



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
        self.book = Book("Scientific Book")
        self.book.format = "PDF"
        self.references_added = False
        self.glossary_added = False
        self.total_pages = 0 

    def add_page(self, content, references=None, glossary=None):
        page_number = PageRegistry()._instance.generate_unique_id()
        page = Page(page_number, content, references=references, glossary=glossary)
        self.book.add_page(page)

        if not self.references_added and references:
            self.references_added = True
            for page in self.book.pages:
                page.add_reference("Sample Reference 1")
                page.add_reference("Sample Reference 2")

        if not self.glossary_added and glossary:
            self.glossary_added = True
            for page in self.book.pages:
                page.add_to_glossary("Sample Term 1", "Sample Definition 1")
                page.add_to_glossary("Sample Term 2", "Sample Definition 2")

        self.total_pages += 1  

class NovelBookBuilder(BookBuilderBase):
    def __init__(self):
        super().__init__()
        self.book = Book("Novel Book")
        self.book.format = "ePub"
        self.characters_added = False
        self.total_pages = 0  

    def add_page(self, content, image_url=None, characters=None):
        page_number = PageRegistry()._instance.generate_unique_id()
        page = Page(page_number, content, image_url=image_url, characters=characters)
        self.book.add_page(page)

        if not self.characters_added and characters:
            self.characters_added = True
            for name, description in characters:
                self.book.add_character(name, description)

        self.total_pages += 1  

class ManualBookBuilder(BookBuilderBase):
    def __init__(self):
        super().__init__()
        self.book = Book("Manual Book")
        self.book.format = "PDF"
        self.total_pages = 0 

    def add_page(self, content, image_url=None):
        page_number = PageRegistry()._instance.generate_unique_id()
        page = Page(page_number, content, image_url)
        self.book.add_page(page)

        self.total_pages += 1  

# Створення книги наукового типу
scientific_book_builder = ScientificBookBuilder()
scientific_book_builder.add_page("Сторінка 1: Вступ", references=["Reference 1", "Reference 2"], glossary=[("Term 1", "Definition 1"), ("Term 2", "Definition 2")])
scientific_book_builder.add_page("Сторінка 2: Розділ 1")
scientific_book_builder.add_page("Сторінка 3: Розділ 2")
scientific_book = scientific_book_builder.get_book()

# Створення книги белетристики
novel_book_builder = NovelBookBuilder()
characters_page1 = [("Character 1", "Description 1"), ("Character 2", "Description 2")]
novel_book_builder.add_page("Сторінка 1: Перший розділ", characters=characters_page1)
novel_book_builder.add_page("Сторінка 2: Другий розділ")
novel_book = novel_book_builder.get_book()

# Створення посібника
manual_book_builder = ManualBookBuilder()
manual_book_builder.add_page("Сторінка 1: Інструкція", "https://i.insider.com/602ee9d81a89f20019a377c6?width=1136&format=jpeg")
manual_book_builder.add_page("Сторінка 2: Додаток", "https://www.meme-arsenal.com/memes/3cb6027ad648c65de50c81876c3a0f60.jpg")
manual_book = manual_book_builder.get_book()


for book in [scientific_book, novel_book, manual_book]:
    print(str(book))
    first_page = True 

    for page in book.get_contents():
        page_number = "Page Id " + str(page.page_number)
        print(f"{page_number}: {page.content}")

        if first_page:  
            if book == scientific_book:
                print("References:")
                for reference in page.references:
                    print(f"- {reference}")
                print("Glossary:")
                for term, definition in page.glossary:
                    print(f"- {term}: {definition}")

            if book == novel_book:
                print("Characters:")
                for name, description in page.characters:
                    print(f"- {name}: {description}")

            first_page = False
