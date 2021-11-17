words = input("Введите список продуктов через пробел: ").split()
print(words)
words = list(words)
len_words = [len(words[i]) for i in range(0, len(words))]
print(len_words)
for ind, words in enumerate(words, 1):
    print(ind, words)










