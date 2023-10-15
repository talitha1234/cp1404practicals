"""
Word Occurrences
Estimate: 30 mins
Actual: 80mins
"""

text = input("Text: ")
words = text.split()
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

# change to list to sort
words = sorted(word_to_count.keys())

longest_word_length = max(len(word) for word in words)

print("\n".join(f'{word:{longest_word_length}}: {word_to_count[word]}' for word in words))
