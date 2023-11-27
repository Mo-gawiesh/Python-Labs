from math import *

print("x < -1")
x = float(input("x = "))
while x >= -1:
    print("Неверный формат входных данных. x < -1")
    x = float(input("x = "))

y = 0
n = 0
try:
    while True:
        member = pow(-1, n + 1) / ((2 * n + 1) * pow(x, 2 * n + 1))
        y += member
        n += 1
except (OverflowError):
    print("y(x) =", -pi / 2 + y)
