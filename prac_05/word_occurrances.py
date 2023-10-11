"""
Word Occurrences
Estimate: 30 mins
Actual: 80mins
"""

text = input("Text: ")
words = text.split()
word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
print(word_to_count)

# change to list to sort
words = sorted(word_to_count.keys())

longest_word_length = max(len(word) for word in words)
for word in words:
    # print each word in the list and key
    print(f'{word:{longest_word_length}}: {word_to_count[word]}')
dict()
