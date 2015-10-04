from collections import Counter

sample_text = 'This is a sample text. This text is being used to count \
occurence of letter in this particular text. This text runs multiple \
lines.'

# dictionary to store letter counts
letter_count = {}

for letter in sample_text:
    # Consider only printbale letters
    if letter == ' ':
        continue
    letter_count[letter] = letter_count.get(letter, 0) + 1

print letter_count

# Print the top 5 most used letters
count = Counter(letter_count)
print "Top 5 most used letters are:"
for (letter, count) in count.most_common(5):
    print "%s : %d" % (letter, count)
