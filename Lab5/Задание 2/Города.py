from random import randint

adjacency_table = []
count_cities = 20
min_len = 10
max_len = 99


def add_node():
    global count_cities
    count_cities += 1

    for i in adjacency_table:
        i.append(0)
    adjacency_table.append([0] * count_cities)

    for i in range(count_cities):
        temp = randint(min_len, max_len)
        adjacency_table[i][count_cities - 1] = temp
        adjacency_table[count_cities - 1][i] = temp


def add_edge(from_citi, to_citi, length):
    adjacency_table[from_citi-1][to_citi-1] = length
    adjacency_table[to_citi-1][from_citi-1] = length


def shortest_path(from_citi, to_citi):
    from_citi-=1
    to_citi-=1
    inf = float("Inf")

    q = [(0, from_citi)]
    d = [inf for i in range(count_cities)]
    d[from_citi] = adjacency_table[from_citi][from_citi]
    while len(q) != 0:
        (cost, u) = q.pop(0)

        for v in range(count_cities):
            if d[v] > d[u] + adjacency_table[u][v]:
                d[v] = d[u] + adjacency_table[u][v]
                q.append((d[v], v))

    to_citi_copy = to_citi
    path = [to_citi_copy + 1]
    while to_citi_copy != from_citi:
        for v in range(count_cities):
            if d[v] == d[to_citi_copy] - adjacency_table[to_citi_copy][v]:
                path.append(v + 1)
                to_citi_copy = v
    path.reverse()


    return d[to_citi], path

def add_in_file_map():
    with open("world.txt", "w") as f:

        f.write("\t\t")
        for i in range(count_cities):
            f.write(str(i + 1) + " ")
            if i < 9:
                f.write(" ")
        f.write("\n")
        f.write("\t")
        for i in range(63):
            f.write("-")
        f.write("\n")
        for i in range(count_cities):
            f.write("%d\t" % (i + 1) + "|")
            f.write("\t")
            for j in range(count_cities):
                f.write(str(adjacency_table[i][j]))
                f.write(" ")
            f.write("\n")


def create_map():
    for i in range(count_cities):
        adjacency_table.append([0] * 20)
    for i in range(count_cities):
        for j in range(count_cities):
            if j >= i:
                temp = randint(min_len, max_len)
                adjacency_table[i][j] = temp
                adjacency_table[j][i] = temp

    add_in_file_map()


print("""Добрый день! Добро рожаловать в нашу карту местнсоти.""")
create_map()
while True:
    print("""\nНа ней на данный момент находятся %d городов.
    Даействия:
    1 -> Показать мир
    2 -> Добавить город
    3 -> Изменить путь от одного города к другому
    4 -> Инфомрация об кратчайшем расстоянии между пунктами
    5 -> Выход""" % (count_cities))
    menu = int(input("\nВыберите действие: "))
    while not 0 < menu < 6:
        print("Неверный формат. От 1 до 5")
        menu = int(input("Выберите действие повторно:"))

    if menu == 1:
        print("Таблица догрог между городами:\n")
        print("\t\t", end="")
        for i in range(count_cities):
            print(i + 1, end=" ")
            if i < 9:
                print(end=" ")
        print()
        print("\t", end="")
        for i in range(63):
            print(end="-")
        print()
        for i in range(count_cities):
            print("%d\t" % (i + 1), end="|")
            print(end="\t")
            for j in range(count_cities):
                print(adjacency_table[i][j], end=" ")
            print()
    elif menu == 2:
        add_node()
        print("Город добавлен")
    elif menu == 3:
        from_citi = int(input("Из какого города (1-%d): " % (count_cities)))
        while not 0 < from_citi < count_cities + 1:
            print("Неверный формат данных")
            from_citi = int(input("Из какого города (1-%d): " % (count_cities)))

        to_citi = int(input("Из какого города (1-%d): " % (count_cities)))
        while not 0 < to_citi < count_cities + 1:
            print("Неверный формат данных")
            to_citi = int(input("Из какого города (1-%d): " % (count_cities)))

        length = int(input("Введите целое значение длины пути (от 10): "))
        add_edge(from_citi, to_citi, length)
        print("Путь изменён")
    elif menu == 4:

        from_citi = int(input("Из какого города (1-%d): " % (count_cities)))
        while not 0 < from_citi < count_cities + 1:
            print("Неверный формат данных")
            from_citi = int(input("Из какого города (1-%d): " % (count_cities)))

        to_citi = int(input("Из какого города (1-%d): " % (count_cities)))
        while not 0 < to_citi < count_cities + 1:
            print("Неверный формат данных")
            to_citi = int(input("Из какого города (1-%d): " % (count_cities)))

        length, path = shortest_path(from_citi, to_citi)
        print("Минимальное расстояние состовляет %d по маршруту"%(length), end=" ")
        for citi in path:
            if citi != path[-1]:
                print(citi, "->", end=" ")
            else:
                print(citi)
    else:
        print("Спасибо, что были с нами!")
        exit()
