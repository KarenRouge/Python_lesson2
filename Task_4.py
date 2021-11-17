words = input("Введите список продуктов через пробел: ").split()
words = list(words)
len_words = [len(words[i]) for i in range(0, len(words))]
i = 0
while len(words[i]) <= 10:
    i = i + 1
    if i == len(words):
        break
k = i
if len(words[k]) <= 10:
    for ind, words in enumerate(words, 1):
        print(ind, words.format)
else:
    long_word = words[k]
words.pop(k)
long_word_cut = long_word[0:9]
words.insert(k, long_word_cut)
words = list(words)
print(words)
for ind, words in enumerate(words, 1):
    print(ind, words.format)
