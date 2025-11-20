# BookBuddy CLI Mockup

from datetime import datetime
import models
import services
import storage
import config

print("welcome to BookBuddy!\nTrack your reading, log progress, and manage your personal library.")
print("===========")
menu = {
    "1":"Add a new book",
    "2":"view all books",
    "3":"Log reading progress",
    "4":"View reading progress",
    "5":"Export book data",
    "6":"Import book data",
    "7":"Exit"
}
print("MAIN MENU")
for key, value in menu.items():
    print(f"{key}. {value}")
print("===========")

while True:
    choice = input("Please enter your choice (1-7):")
    if choice == "1":
         book_title = input("Enter book title:")
         author_name = input("Enter author name:")
         genre = input("Enter genre:")
         while True:
             try:
                 total_pages = int(input("enter total pages:"))
                 break
             except:
                 print("please enter a valid number")
                 continue
         New_book = models.Book.add_new_book(book_title, author_name, genre,total_pages)
    elif choice == "2":
         print("your library:")
         for i in models.Book.all_books:
              print(f"- {i.book_title} by {i.author_name} , [{i.genre}], {i.total_pages} pages")
    elif choice == "3":
        book_title = input("Enter book title:")
        while True:
            try:
                read_pages =int(input("enter read pages:"))
                break 
            except:
                   print("please enter a valid number:")
                   continue
        while True:
            try:
                total_pages = int(input("enter total pages:"))
                break
            except:
                  print("please enter a valid number")
                  continue
            
        book_found = False
        for i in models.Book.all_books:
            if book_title == i.book_title:
                new = models.Readinglog(book_title,total_pages, read_pages)
                models.Readinglog.reading_books.append(new)
                book_found = True
                print("Reading log added!")
                break
        
        if not book_found:
            print("any book not found with book title. please enter another")
            
    elif choice == "4":
     results = services.reading_progress()
     for result in results:
          print(f"{result[0]} - {result[1]}/{result[2]} pages read ({result[3]}%)")

    elif choice == "5":
         storage.export_data()
        

    elif choice == "6":
         storage.import_data()

    elif choice == "7":
        print("Thanks for using BookBuddy!")
        exit()
            

   
    
            
    
        
            
            
        
   
 
