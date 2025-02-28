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

    print(f"{get_num_words(frankenstein_text)} words found in the document")
    print(f"{get_num_char(frankenstein_text)}")


main()