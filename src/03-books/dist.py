from utils.measure import measure_elapsed_time
from prefect import task, flow
from shared import read_books_data, write_result, normalize_book, append_unique_authors

@task
def write_data(books, authors, mappings):
    write_result(books, authors, mappings)

@task
def process_entry(entry):
    return normalize_book(entry)

@task
def combine_results(results):
    books = []
    authors = []
    mappings = []

    for result in results:
        book, author_list, author_mapping = result
        books.append(book)
        authors = append_unique_authors(authors, author_list)
        mappings.extend(author_mapping)

    return books, authors, mappings

@measure_elapsed_time
@flow
def book_flow(data):
    results = process_entry.map(data)
    books, authors, mappings = combine_results(results)
    write_data(books, authors, mappings)

if __name__ == '__main__':
    data = read_books_data()
    book_flow(data)