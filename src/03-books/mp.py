
from multiprocessing import Pool, cpu_count, freeze_support
from shared import normalize_book, append_unique_authors, read_books_data, write_result
from utils.measure import measure_elapsed_time
from utils.data import write_file


@measure_elapsed_time
def process_data_multiprocessing(data):
    books = []
    authors = []
    mappings = []

    pool = Pool(cpu_count())
    results = pool.map(normalize_book, data)
    pool.close()
    pool.join()

    for result in results:
        book, author_list, author_mapping = result
        books.append(book)
        authors = append_unique_authors(authors, author_list)
        mappings.extend(author_mapping)

    return books, authors, mappings

if __name__ == '__main__':
    freeze_support()
    data = read_books_data()
    books, authors, mappings = process_data_multiprocessing(data)
    write_result(books, authors, mappings)