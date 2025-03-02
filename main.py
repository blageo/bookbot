from stats import get_num_words
from stats import get_num_char

def get_book_test(path):
    contents = ''

    with open("books/frankenstein.txt") as f:
        contents = f.read()

    return contents


def main():
    path_to_book="books/frankenstein.txt"
    frankenstein_text=get_book_test(path_to_book)
    num_words = get_num_words(frankenstein_text)
    char_dict = get_num_char(frankenstein_text)
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