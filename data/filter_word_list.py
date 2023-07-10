from string import ascii_lowercase as valid_letters

min_length = 4

with open('words.txt', 'r', encoding='utf-8') as infile, open('words_usable.txt', 'w', encoding='utf-8') as outfile:
	for line in infile:
		word = line.strip()
		if len(word) < min_length: continue
		valid = True
		for c in word:
			if c not in valid_letters:
				valid = False
				break
		if valid: outfile.write(word + '\n')