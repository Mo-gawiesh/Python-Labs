num = int(input("Трёхзначное число = "))
a = num // 100
b = num // 10 % 10
c = num % 10
print("Сумма цифр:", a + b + c)
print("Произведение цифр:", a * b * c)
