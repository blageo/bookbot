import sys
from stats import get_num_words
from stats import get_num_char

def get_book_test(path):
    with open(sys.argv[1]) as f:
        contents = f.read()

    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]
    book_text=get_book_test(path_to_book)
    num_words = get_num_words(book_text)
    char_dict = get_num_char(book_text)
    sorted_dict = dict(sorted(char_dict.items(), key = lambda item: item[1], reverse = True))

    # Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_dict:
        if i.isalpha():
            print(f"{i}: {sorted_dict[i]}")
    print("============= END ===============")
    

main()