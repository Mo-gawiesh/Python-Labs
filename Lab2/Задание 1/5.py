from math import *

print("|x| <= 1")
x = float(input("x = "))
while abs(x) > 1:
    print("Неверный формат входных данных. |x| <= 1")
    x = float(input("x = "))

y = 0
n = 0
try:
    while True:
        member = (pow(-1, n) * pow(x, 2 * n + 1)) / (2 * n + 1)
        y += member
        n += 1
        if  abs(member) < 1e-18:
            raise OverflowError
except (OverflowError):
    print("y(x) =", y)
