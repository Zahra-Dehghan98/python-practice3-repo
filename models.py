from datetime import datetime


class Book:
    all_books = []
    def __init__(self, book_title:str ,author_name:str, genre:str, total_pages:str):
        self.book_title = book_title
        self.author_name = author_name
        self.genre = genre
        self.total_pages = total_pages
        self.datetime = datetime.now()

    @classmethod
    def add_new_book(self, book_title:str ,author_name:str, genre:str, total_pages:str): 
        new_book = Book(book_title, author_name, genre, total_pages)
        Book.all_books.append(new_book) 
        print(f" Book '{book_title}' added successfully!")

class Ebook(Book):
    def __init__(self, book_title:str ,author_name:str, genre:str, total_pages:str, format:str, size:int, language:str):
        self.format = format
        self.size = size
        self.language = language
        super().__init__(book_title, author_name, genre, total_pages)

class Audiobook(Ebook):
    def __init__(self, book_title, author_name, genre, audio_format:str, audio_size:str, language, narrator:str,total_duration:str):
        self.audio_size = audio_size
        self.audio_format = audio_format
        self.narrator = narrator
        self.total_duration = total_duration
        super().__init__(book_title, author_name, genre, language)

class Readinglog:
    reading_books = []
    def __init__(self, book_title:str, total_pages:int, read_pages:int):
        self.total_pages = total_pages
        self.book_title = book_title
        self.read_pages = read_pages
        self.datetime = datetime.now()
     


                 
                 

