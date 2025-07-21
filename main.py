import sys
from stats import word_count, char_count, sort_on, sort_characters

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		return f.read()

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	path = sys.argv[1]
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	full = get_book_text(path)
	words = full.split()
	word_count = len(words)
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	character_count = char_count(full)
	sorted_chars = sort_characters(character_count)
	for item in sorted_chars:
		char = item["char"]
		if char.isalpha():
			print(f"{char}: {item['num']}")
	print("============= END ===============")

main()
