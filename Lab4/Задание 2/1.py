from math import sqrt

def rec(n, left, right):
    root = (right-left)/2 + left
    if sqrt(2) - n <= root <= sqrt(2) + n:
        return root
    else:
        if root > sqrt(2):
            return rec(n, left, root)
        else:
            return rec(n, root, right)

n = float(input("Введите точность: "))
print(rec(n, 0, 5))
