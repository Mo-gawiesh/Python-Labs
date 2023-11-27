def a(n):
    temp_set = {i for i in range(1, n + 1) if i % 7 == 0}
    if not temp_set:
        temp_set.add("таких чисел нет")
    return temp_set


def b(n):
    temp_list = [i for i in range(2, n)]
    p = 1
    is_possible = True
    while is_possible and temp_list and p <= n:
        for i in temp_list:
            if i > p:
                p = i
                break
        is_possible = False
        temp = []
        for val in temp_list:
            if val % p == 0 and val != p:
                is_possible = True
            else:
                temp.append(val)
        temp_list = temp.copy()
    if not temp_list:
        temp_list.append("нет")
    return temp_list


n = int(input("n = "))
print("а) Числа от до %d кратные 7:" % (n), *a(n))
print("б) Все простые числа от 1 до n:", *b(n))
