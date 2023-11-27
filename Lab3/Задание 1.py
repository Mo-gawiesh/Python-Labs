input_string = input()
print("Длина строки:", len(input_string))
print("Количество слов в строке:", len(input_string.split()))
print("Длина самого короткого слова:", len(min(input_string[:-1].split())))
print("Длина самого длинного слова:", len(max(input_string[:-1].split())))

update_string = ""
for i in input_string:
    if i != "*":
        update_string += i+i
print("Преобраованная строка:", update_string)

