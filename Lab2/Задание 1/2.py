from math import *

x = float(input("x = "))

y = 0
n = 0
try:
    while True:
        member = (pow(-1, n) * pow(x, n)) / factorial(n)
        y += member
        n += 1
except (OverflowError):
    print("y(x) =", y)
