import sys
from stats import get_word_count, get_char_count, sorted_list, sort_on

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    print(contents)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------""")
    get_word_count(sys.argv[1])
    print("--------- Character Count -------")
    sorted_list(get_char_count(sys.argv[1]))

main()