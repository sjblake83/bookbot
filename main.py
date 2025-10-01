from stats import get_word_count, get_character_counts

def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)
 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(get_word_count(book_contents))
    print(get_character_counts(book_contents))
    print("============= END ===============")
    
def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

main()