import sys
from stats import get_num_of_words, get_char_counts_dict, char_counts_dict_to_sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def print_report(book_path, word_count, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for item in chars_sorted_list:
        char = item["char"]
        count = item["count"]
        
        if char.isalpha():
            print(f"{char}: {count}")

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    word_count = get_num_of_words(text)
    char_counts_dict = get_char_counts_dict(text)
    sorted_list = char_counts_dict_to_sorted_list(char_counts_dict)
    print_report(book_path, word_count, sorted_list)
    
    

main()