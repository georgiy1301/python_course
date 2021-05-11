words = input('Введите несколько слов: ')
words = words.split()
words = list(words)
for index, value in enumerate(words):
    print(index + 1, value[:10])