from random import randint

def _1():
    rev = rnum_list[::-1]
    is_del = False
    start = n-1
    finish = n-1
    for i in range(len(rev)-1):
        if rev[i] > 0:
            if rev[i + 1] > 0:
                if not is_del:
                    is_del = True
                    start = i
            elif is_del:
                finish = i
                break

    rev[start:finish+1] = []
    return rev[::-1]


def _2():
    min_ind = rnum_list.index(min(rnum_list))
    temp = []
    for i in range(min_ind+1, len(rnum_list)-1):
        if rnum_list[i] > 0:
            temp.append(rnum_list[i])
        else:
            if i == min_ind+1:
                if rnum_list[i] <= 0 and rnum_list[i+1] >= 0:
                    temp.append(rnum_list[i])
            else:
                if rnum_list[i - 1] >= 0 and rnum_list[i] <= 0 and rnum_list[i + 1] >= 0:
                    temp.append(rnum_list[i])
    return rnum_list[:min_ind+1] + temp


def _3():
    min_ind = rnum_list.index(min(rnum_list))
    temp = []
    for i in range(min_ind):
        if rnum_list[i] >= 0:
            temp.append(rnum_list[i])
    return temp + rnum_list[min_ind:]

def _4():
    min_ind = rnum_list.index(min(rnum_list))
    temp = []
    if min_ind != 0:
        prev = min_ind-1
        for i in rnum_list:
            if rnum_list[prev] <= i:
                temp.append(i)
    return temp


def _5():
    pos, neg = [], []
    temp = []
    for i in rnum_list:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
    min_pos, max_neg = 0, 0
    if pos:
        min_pos = min(pos)
    if neg:
        max_neg = max(neg)
    for i in rnum_list:
        if i <= max_neg or i >= min_pos:
            temp.append(i)
    return temp


def _6():
    min_ind = rnum_list.index(min(rnum_list))
    temp = []
    for i in range(min_ind, len(rnum_list)):
        if (i+1) % 2 != 0 or rnum_list[i] <= 0:
            temp.append(rnum_list[i])

    return temp


def _7():
    temp = [rnum_list[0]]
    for i in range(1, len(rnum_list)-1):
        if not(rnum_list[i-1] > 0 and rnum_list[i] < 0 and rnum_list[i+1] > 0):
            temp.append(rnum_list[i])
    temp.append(rnum_list[-1])
    return temp

def _8():
    temp = []
    for i in range(len(rnum_list)-1):
        if rnum_list[i] != rnum_list[i+1]:
            temp.append(rnum_list[i])
    temp.append(rnum_list[-1])
    return temp

def _9():
    pos = []
    for i in range(len(rnum_list)):
        if rnum_list[i] >= 0:
            pos.append(i)
    ind = 1
    temp = rnum_list[:pos[0]]
    for i in range(len(pos)-1):
        if pos[i+1] - pos[i] < 3 or rnum_list[pos[i+1]] == 0 or rnum_list[pos[i]] == 0:
            temp += rnum_list[pos[i]:pos[i+1]]
        else:
            temp.append(rnum_list[pos[i]])
    temp+=rnum_list[pos[-1]:]

    return temp


def _10():
    pos, neg = [], []
    temp = []
    for i in rnum_list:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
    min_pos, max_neg = 0, 0
    if pos:
        min_pos = min(pos)
    if neg:
        max_neg = max(neg)
    for i in rnum_list:
        if i <= max_neg or i >= min_pos:
            temp.append(i)
    return temp


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
