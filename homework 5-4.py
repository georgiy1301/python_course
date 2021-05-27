ru = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре" }
with open('for_homework_4.txt', 'w', encoding='utf-8') as nf:
    with open('for_homework_4_1.txt', 'r', encoding='utf-8') as mf:
        nf.write(str([line.replace(line.split()[0], ru.get(line.split()[0])) for line in mf]))

from googletrans import Translator
with open('for_homework_4.txt', 'w', encoding='utf-8') as nf:
    with open('for_homework_4_1.txt', 'r', encoding='utf-8') as mf:
        text = mf.read()
    t = Translator()
    a = t.translate(text)
    print(a)