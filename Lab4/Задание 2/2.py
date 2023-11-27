def evklid(m, n):
    if m > n:
        return evklid(m - n, n)
    if m < n:
        return evklid(n, m)
    else:
        return m


n = float(input("n = "))
while n <= 0:
    print("Нельзя вводить", n)
    n = float(input("n = "))
m = float(input("m = "))
while m <= 0:
    print("Нельзя вводить", m)
    n = float(input("m = "))
print(evklid(n,m))
