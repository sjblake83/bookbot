def get_word_count(book_text):
    split_words = book_text.split()
    word_count_formatted = __format_word_count_for_printing(len(split_words))
    return word_count_formatted

def get_character_counts(book_text):
    text_lower = book_text.lower()
    char_dictionary = {}
    for char in text_lower:
        char_dictionary[char] = char_dictionary.get(char, 0) + 1
    char_count_sorted = __get_char_count_sorted_list(char_dictionary)
    char_count_formatted = __format_char_count_for_printing(char_count_sorted)
    return char_count_formatted

def __get_char_count_sorted_list(char_dictionary):
    chars_sorted = sorted(
        list(char_dictionary.items()), 
        key=lambda x: x[1], 
        reverse=True)
    return chars_sorted

def __format_word_count_for_printing(word_count):
    print_output = "----------- Word Count ----------\n"
    print_output += f"Found {word_count} total words"
    return print_output

def __format_char_count_for_printing(char_counts):
    print_output = ["--------- Character Count -------"]
    for key, value in char_counts:
        print_output.append(f"{key}: {value}")
    return "\n".join(print_output)