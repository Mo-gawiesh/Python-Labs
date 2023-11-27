from random import uniform, randint


def _1(n, m):
    matrix = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(uniform(-10, 10))
        matrix.append(temp)

    max_el, min_el, max_ind, min_ind = matrix[0][0], matrix[0][0], [0, 0], [0, 0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_el:
                max_el = matrix[i][j]
                max_ind = [i, j]
            if matrix[i][j] < min_el:
                min_el = matrix[i][j]
                min_ind = [i, j]
    print("max:", f"ind = {max_ind[0], max_ind[1]},", "value =", max_el)
    print("min:", f"ind = {min_ind[0], min_ind[1]},", "value =", min_el)


def _2(n, m):
    matrix = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(uniform(-10, 10))
        matrix.append(temp)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = abs(matrix[i][j])
            print(matrix[i][j], end=" ")
        print()


def _3(n, m):
    matrix = []
    middle = [0] * m
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(uniform(-10, 10))
        matrix.append(temp)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            middle[j] += matrix[i][j]
            print(matrix[i][j], end=" ")
        print()

    print("среднее арифметическое:")
    for i in middle:
        print(i / n, end=" ")
    print()


def _4(n, m):
    matrix = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(uniform(-10, 10))
        matrix.append(temp)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] **= 2
            print(matrix[i][j], end=" ")
        print()


def _5(n, m):
    matrix = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(randint(-10, 10))
        matrix.append(temp)
    pos_count, neg_count = 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0:
                pos_count += 1
            elif matrix[i][j] < 0:
                neg_count += 1
    print("количество положительных чисел: %d\nколичество отрицательных чисел: %d" % (pos_count, neg_count))


def _6(n, m):
    matrix = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(randint(-10, 10))
        matrix.append(temp)

    max_el, max_ind = matrix[0][0], [0, 0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i + j) % 2 != 0:
                if matrix[i][j] > max_el:
                    max_el = matrix[i][j]
                    max_ind = [i, j]

    print("max:", f"ind = {max_ind[0], max_ind[1]},", "value =", max_el)


def _7(n, m):
    matrix = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(randint(-10, 10))
        matrix.append(temp)

    even, odd = 0, 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 2 == 0:
                even += 1
            else:
                odd += 1

    print("количество четных:", even)
    print("количество нечетных:", odd)


def _8(n, m):
    matrix = []
    middle = [0] * n
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(uniform(-10, 10))
        matrix.append(temp)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            middle[i] += matrix[i][j]
            print(matrix[i][j], end=" ")
        print()

    print("среднее арифметическое:")
    for i in middle:
        print(i / m, end=" ")
    print()


def _9(n, m):
    matrix = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(uniform(-10, 10))
        matrix.append(temp)

    zer_main_diog, zer_diog = 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j and matrix[i][j] == 0:
                zer_main_diog += 1
            elif i + j == n - 1 and matrix[i][j] == 0:
                zer_diog += 1

    print("Кол-во нулевых элементов на главной диагонали:", zer_main_diog)
    print("Кол-во нулевых элементов на побочной диагонали:", zer_diog)

def _10(n,m,k):
    matrix = []
    el = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(randint(-10, 10))
        matrix.append(temp)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % k == 0:
                el.append([matrix[i][j], [i,j], matrix[i][j] // k])

    for i in el:
        print("Элемент: %d, индексы: (%d, %d), степень кратности: %d"%(i[0], i[1][0], i[1][1], i[2]))

n = int(input("n = "))
m = int(input("m = "))

print("1.")
_1(n, m)
print()

print("2.")
_2(n, m)
print()

print("3.")
_3(n, m)
print()

print("4.")
_4(n, m)
print()

print("5.")
_5(n, m)
print()

print("6.")
_6(n, m)
print()

print("7.")
_7(n, m)
print()

print("8.")
_8(n, m)
print()

print("9.")
_9(n, m)
print()

print("10.")
k = int(input("k = "))
_10(n, m, k)
print()
