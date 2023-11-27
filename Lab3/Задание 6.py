from random import randint

left_bound = -10
right_bound = 10
n = 3
m = 5
k = 7


T = []
for i in range(n):
    temp_m =  []
    for j in range(m):
        temp_k = []
        for l in range(k):
            temp_k.append(randint(left_bound, right_bound))
        temp_m.append(temp_k)
    T.append(temp_m)
max_num, ind_max = T[0][0][0], [0,0,0]

for i in range(n):
    for j in range(m):
        for l in range(k):
            if T[i][j][l] > max_num:
                max_num = T[i][j][l]
                ind_max = [i,j,k]

print("Наибольшее число: %d, индексы: (%d, %d, %d)"%(max_num, ind_max[0], ind_max[1], ind_max[2]))