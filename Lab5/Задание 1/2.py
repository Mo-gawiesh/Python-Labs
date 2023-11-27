with open("in.txt", "r", encoding='utf-8') as fi:
    text = fi.readlines()
word_from = input("Введите слово какое заменить: ")
word_to = input("Введите слово на какое заменить: ")
with open("out.txt", "w", encoding='utf-8') as fo:
    for i, line in enumerate(text):
        line = line.replace(word_from, word_to)
        fo.writelines(line)
print("Слово %s в тексте заменено на слово %s"%(word_from, word_to))


