from stats import get_word_count

def main():
    book_contents = get_book_text("books/frankenstein.txt")
    book_word_count = get_word_count(book_contents)
    print(f"Found {book_word_count} total words")

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

main()