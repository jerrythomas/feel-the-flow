import os
import json
from utils.data import write_file

def normalize_book(entry):
    book = {"book_id": entry["book_id"], "book_title": entry["book_title"]}
    author_list = entry["authors"]
    author_book_mapping = []

    for author in entry["authors"]:
        author_book_mapping.append({"book_id": entry["book_id"], "author": author})

    return book, author_list, author_book_mapping

def append_unique_authors(authors, new_authors):
    for author in new_authors:
        if author not in authors:
            authors.append(author)
    return authors

def read_books_data():
		with open(os.path.join(os.environ['DATA_DIR'], "books.json"), 'r') as file:
				data = json.load(file)
		return data

def write_result(books, authors, mappings):
		print(f"Found {len(books)} books")
		print(f"Found {len(authors)} authors")
		print(f"Found {len(mappings)} mappings")

		write_file(os.path.join(os.environ['DATA_DIR'],"output", "authors.json"), authors)
		write_file(os.path.join(os.environ['DATA_DIR'],"output", "books.json"), books)
		write_file(os.path.join(os.environ['DATA_DIR'],"output", "mappings.json"), mappings)