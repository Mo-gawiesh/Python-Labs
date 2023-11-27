print("x > 0")
x = float(input("x = "))
while x <= 0:
    print("Неверный формат входных данных. x > 0")
    x = float(input("x = "))

y = 0
n = 0
try:
    while True:
        member = pow(x - 1, 2 * n + 1) / ((2 * n + 1) * pow(x + 1, 2 * n + 1))
        y += member
        n += 1
except (OverflowError):
    print("y(x) =", 2 * y)
