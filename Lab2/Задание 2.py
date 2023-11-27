text = input("Введиет фразу: ")
while len(text) < 10:
    print("Неверный формат данных.\nВ фраза должна быть больше 10 символов")
    text = input("Введиет фразу: ")

print("a) первые 4 символа: " + text[:4])
print("б) последние 4 символа: " + text[-4:])
if len(text) % 2 == 0:
    print("в) символ посередине: " + text[len(text) // 2] + " или " + text[len(text) // 2 - 1])
else:
    print("в) символ посередине: " + text[len(text) // 2])
print("г) символы с 3-го по 8-й: " + text[2:8])
