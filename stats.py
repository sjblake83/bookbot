def get_word_count(book_text):
    split_words = book_text.split()
    return len(split_words)

def get_character_counts(book_text):
    text_lower = book_text.lower()

    char_dictionary = {}
    
    for char in text_lower:
        if char not in char_dictionary:
            char_dictionary.update({char : 1})
        else:
            char_dictionary[char] += 1
    return char_dictionary