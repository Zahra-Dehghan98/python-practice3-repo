import models

def reading_progress():
    results = []
    for b1 in models.Book.all_books:
        total_read = 0
        for b2 in models.Readinglog.reading_books:
            if b2.book_title == b1.book_title:
                total_read = total_read + b2.read_pages
        progress_percentage =float((total_read/b1.total_pages)*100)
        results.append([b1.book_title, total_read, b1.total_pages, progress_percentage])
    return results
    


        
    
        