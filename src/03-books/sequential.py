from shared import normalize_book, append_unique_authors, read_books_data, write_result
from utils.data import write_file
from utils.measure import measure_elapsed_time

@measure_elapsed_time
def process_data_sequentially(data):
    books = []
    authors = []
    mappings = []

    for entry in data:
        book, author_list, author_book_mapping = normalize_book(entry)
        books.append(book)
        authors = append_unique_authors(authors, author_list)
        mappings.extend(author_book_mapping)

    return books, authors, mappings

if __name__ == '__main__':
    data = read_books_data()
    books, authors, mappings = process_data_sequentially(data)
    write_result(books, authors, mappings)
