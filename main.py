import sys
from stats import count_words, count_characters, sort_on

def get_book_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    data = get_book_text(book)
    count = count_words(data)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    character_count = count_characters(data)
    character_count.sort(reverse=True, key=sort_on)
    for character in character_count:
        print(f"{character['char']}: {character['num']}")
    print("============= END ===============")


main()