def get_num_words(path):
    num_words = 0
    book_list = path.split()
    
    for i in book_list:
        num_words += 1
    
    return num_words

def get_num_char(path):
    char_dict = {}


    for char in path:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict