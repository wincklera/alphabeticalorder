file = input("Enter the input file name:")
f = open(file, 'r')
words = f.read()
unique_words = sorted(words.split(' '))
for word in words.split():
    if unique_words.count(word) > 1:
      value = word
      unique_words.remove(value)
    else:
        print(word)

unique_words = sorted(set(words.split(' ')))
print(unique_words)