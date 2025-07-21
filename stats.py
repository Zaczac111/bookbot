import sys
def word_count():
	path = sys.argv[1]
	full = get_book_text(path)
	words = full.split()
	word_count = len(words)
	return word_count

def char_count(text):
	lower = text.lower()
	characters = {}
	for char in lower:
		if char in characters:
			characters[char] += 1
		else:
			characters[char] = 1
	return characters

def sort_on(item):
	return item["num"]

def sort_characters(characters):
	char_list = [{"char": c, "num": n} for c, n in characters.items()]
	char_list.sort(reverse=True, key=sort_on)
	return char_list
