try:
    a = list(map(int, input("Последовательность чисел: ").split(",")))
    if len(a) != 6:
        raise Exception
except (Exception):
    print("Неверный формат данных.\nВведите 6 целых десятичных чисел через запятую без пробела")
    a = list(map(int, input("Последовательность чисел: ").split(",")))

print("a) 4-й элемент: " + str(a[3]))
print("б) все элементы в обратном порядке:", *a[::-1])
print("в) сумма: %f, среднее арифметическое: %f"%(sum(a), sum(a)/len(a)))