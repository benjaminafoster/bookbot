import sys
from stats import count_words, character_count, char_dict_to_sorted_list

def get_book_text(filepath):
    with open(filepath, 'r') as fp:
        filecontent = fp.read()
    return filecontent

def print_report(book_path, num_words, char_sorted_list):
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char in char_sorted_list:
            if char["char"].isalpha():
                print(f"{char["char"]}: {char["count"]}")
        print("============= END ===============")

def main():
    if len(sys.argv) != 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    num_words = count_words(book_content)
    character_count_dict = character_count(book_content)
    char_sorted_list = char_dict_to_sorted_list(character_count_dict)
    print_report(book_path, num_words, char_sorted_list)

main()