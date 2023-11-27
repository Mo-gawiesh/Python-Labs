with open("in.txt", "r", encoding='utf-8') as f:
    text = f.readlines()
    count = 0
    word = input("Введите слово: ")
    for i, line in enumerate(text):
        line = line.strip()
        count += line.count(word)

print("Слово %s в тексте встречается %d раз(-а)"%(word, count))


