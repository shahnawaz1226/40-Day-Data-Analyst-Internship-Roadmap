'''Take a sentence and print:
total unique characters
total characters (excluding spaces)
total words'''

sentence = input("Enter sentence: ").lower()

unq_char_count = len(set(sentence))
char_count = len(sentence.replace(" ", ""))
total_words = len(sentence.split())

print(f"Total unique characters: {unq_char_count}")
print(f"Total characters (excluding spaces): {char_count}")
print(f"Total words: {total_words}")