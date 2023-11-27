from random import randint


def _1():
    max_pos = 0
    temp_max_pos = 0
    ind = [0, 0]
    from_ind = 0
    for i in range(len(rnum_list)):
        if rnum_list[i] > 0:
            if temp_max_pos == 0:
                from_ind = i
            temp_max_pos += 1
        else:
            temp_max_pos = 0
        if max_pos < temp_max_pos:
            ind[0] = from_ind
            ind[1] = i
            max_pos = temp_max_pos

    return rnum_list[ind[0]:ind[1] + 1] + rnum_list[:ind[0]] + rnum_list[ind[1] + 1:]


def _2():
    temp_list = rnum_list.copy()
    count_zeros = 0
    res = []
    while temp_list.count(0):
        temp_list.remove(0)
        count_zeros += 1
    if temp_list:
        max_ind = temp_list.index(max(temp_list))
        for i in range(len(temp_list)):
            res.append(temp_list[i])
            if i == max_ind:
                for i in range(count_zeros):
                    res.append(0)
    else:
        for i in range(count_zeros):
            res.append(0)
    return res


def _3():
    pos, neg = [], []
    for i in rnum_list:
        if i >= 0:
            pos.append(i)
        else:
            neg.append(i)
    return pos + neg


def _4():
    min_num = min(rnum_list)
    pos, neg = [], []
    for i in rnum_list:
        if i == min_num:
            break
        if i > 0:
            pos.append(i)
        else:
            neg.append(i)
    return neg + rnum_list[rnum_list.index(min_num):] + pos


def _5():
    pos = []
    temp = []
    is_first_pos = True
    for i in rnum_list:
        if i > 0:
            if not is_first_pos:
                pos.append(i)
            else:
                temp.append(i)
                is_first_pos = False
        else:
            temp.append(i)
    return temp + pos


def _6():
    max_pos = 0
    temp_max_pos = 0
    ind = [0, 0]
    from_ind = 0
    for i in range(len(rnum_list)):
        if rnum_list[i] < 0:
            if temp_max_pos == 0:
                from_ind = i
            temp_max_pos += 1
        else:
            temp_max_pos = 0
        if max_pos < temp_max_pos:
            ind[0] = from_ind
            ind[1] = i
            max_pos = temp_max_pos

    return rnum_list[:ind[0]] + rnum_list[ind[1] + 1:] + rnum_list[ind[0]:ind[1] + 1]


def _7():
    neg = []
    temp = []
    for i in range(len(rnum_list)):
        if (i + 1) % 2 != 0 and rnum_list[i] < 0:
            neg.append(rnum_list[i])
        else:
            temp.append(rnum_list[i])
    return temp + neg


def _8():
    pos = []
    temp = []
    for i in range(len(rnum_list)):
        if (i + 1) % 2 == 0 and rnum_list[i] > 0:
            pos.append(rnum_list[i])
        else:
            temp.append(rnum_list[i])
    return pos + temp


def _9():
    neg = []
    temp = []
    for i in range(len(rnum_list)):
        if (i + 1) % 2 == 0 and rnum_list[i] < 0:
            neg.append(rnum_list[i])
        else:
            temp.append(rnum_list[i])
    return neg + temp


def _10():
    max_pos = 0
    temp_max_pos = 0
    ind = [0, 0]
    from_ind = 0
    for i in range(len(rnum_list)):
        if rnum_list[i] > 0:
            if temp_max_pos == 0:
                from_ind = i
            temp_max_pos += 1
        else:
            temp_max_pos = 0
        if max_pos < temp_max_pos:
            ind[0] = from_ind
            ind[1] = i
            max_pos = temp_max_pos

    return rnum_list[:ind[0]] + rnum_list[ind[1] + 1:] + rnum_list[ind[0]:ind[1] + 1]


n = int(input("Введите длину желаемого списка: "))
rnum_list = []
for i in range(n):
    rnum_list.append(randint(-10, 10))

print("Рандомный список:", *rnum_list)
print()
print("1. ", *_1())
print("2. ", *_2())
print("3. ", *_3())
print("4. ", *_4())
print("5. ", *_5())
print("6. ", *_6())
print("7. ", *_7())
print("8. ", *_8())
print("9. ", *_9())
print("10. ", *_10())
