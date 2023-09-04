import os
import random
import argparse
from data import write_file

def generate_authors(num_authors):
    authors = []
    for author_id in range(1, num_authors + 1):
        author = {
            "author_id": author_id,
            "author_name": f"Author {author_id}"
        }
        authors.append(author)
    return authors


def generate_books(num_books, authors, max_authors_per_book=3):
    books = []
    for book_id in range(1, num_books + 1):
        book = {
            "book_id": book_id,
            "book_title": f"Book Title {book_id}",
            "authors": random.sample(authors, random.randint(2, max_authors_per_book))
        }
        books.append(book)
    return books

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_authors", type=int, default=100)
    parser.add_argument("--num_books", type=int, default=100)
    parser.add_argument("--max_authors_per_book", type=int, default=3)
    parser.add_argument("--books_file", type=str, default="books.json")
    return parser.parse_args()

def main():
    args = parse_args()

    authors = generate_authors(args.num_authors)
    books = generate_books(args.num_books, authors, args.max_authors_per_book)
    file_path = os.path.join(os.environ['DATA_DIR'], args.books_file)
    write_file( file_path, books)

if __name__ == "__main__":
    main()
