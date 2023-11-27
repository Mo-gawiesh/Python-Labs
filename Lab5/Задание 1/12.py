with open("in.txt", "r", encoding='utf-8') as f:
    text = f.readlines()
    count_alpha = 0
    coun_digit = 0
    for i, line in enumerate(text):
        line = line.strip()
        for letter in line:
            if letter.isalpha():
                count_alpha += 1
            elif line.isdigit():
                coun_digit += 1
if count_alpha > coun_digit:
    print("Латинских букв больше")
elif coun_digit > count_alpha:
    print("Цифр больше")
else:
    print("Количество латинских букв и цифр одинаково")
