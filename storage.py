import models
import json 
import pickle
import config


def export_data():
    all_data = {
    "all_books": [{"title": book.book_title, "author": book.author_name, "genre": book.genre, "pages": book.total_pages}
        for book in models.Book.all_books],
    "readinglogs":[{"book_title": log.book_title, "read_pages": log.read_pages, "total_pages": log.total_pages}
        for log in models.Readinglog.reading_books
]
}
    file_name = input("enter filename:")
    
    while True:
        ex_format = input("enter format:")
        if ex_format.lower() == "json":
            with open(file_name, "w")as file :
                json.dump(all_data, file, indent=4)
                break
        elif ex_format.lower() == "pickle":
            with open(file_name, "wb")as file :
                pickle.dump(all_data, file)
                break
        else:
             ex_format = config.default_file_format
             print(f"invalid format! use default: {ex_format}")
             with open(file_name, "w")as file :
                json.dump(all_data, file, indent=4)
                break

def import_data():
    while True:
        file_name = input("enter filename:")
        if file_name.endswith("json"):
            with open(file_name, "r") as file:
                loaded = json.load(file)
                for book_data in loaded["all_books"]:
                    models.Book.add_new_book(book_data["title"], book_data["author"], book_data["genre"], book_data["pages"])
                for log_data in loaded["readinglogs"]:
                    log = models.Readinglog(log_data["book_title"], log_data["read_pages"], log_data["total_pages"])
                    models.Readinglog.reading_books.append(log)
                break
        elif file_name.endswith("pickle"):
            with open(file_name, "rb") as file:
                loaded = pickle.load(file)
                for book_data in loaded["all_books"]:
                    models.Book.add_new_book(book_data["title"], book_data["author"], book_data["genre"], book_data["pages"])
                for log_data in loaded["readinglogs"]:
                    log = models.Readinglog(log_data["book_title"], log_data["read_pages"], log_data["total_pages"])
                    models.Readinglog.reading_books.append(log)
                break
        else:
            print("open a file with valid format (json or pickle)")
        continue
