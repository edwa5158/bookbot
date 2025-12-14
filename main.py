from stats import count_words, count_chars, sort_chars
import sys

def get_book_test(path_to_file: str)->str:
    with open(path_to_file) as f:
        return f.read()

def main():
    # path_to_file: str = "books/frankenstein.txt"
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file: str = sys.argv[1]
    
    contents: str = get_book_test(path_to_file)
    total_words:int = count_words(contents)
    chars: dict[str, int] = count_chars(contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for char in sort_chars(chars):
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

main()