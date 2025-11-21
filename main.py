from stats import get_word_count, get_char_count, sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    print(contents)

def main():
    get_word_count("books/frankenstein.txt")
    get_char_count("books/frankenstein.txt")

sorted_list(get_char_count("books/frankenstein.txt"))
