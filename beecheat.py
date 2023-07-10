from sys import argv, exit
from string import ascii_uppercase

if len(argv) != 2:
	exit()
	
letters = argv[1]

magic_letter = ''
for c in letters:
	if c in ascii_uppercase:
		magic_letter = c.lower()
		break

letters = letters.lower()

words = []
with open('data/words_usable.txt', 'r', encoding='utf-8') as infile:
	for line in infile:
		word = line.strip()
		usable = True
		for c in word:
			if c not in letters:
				usable = False
				break
			if magic_letter not in word:
				usable = False
		if usable: words.append(word)

print(words)