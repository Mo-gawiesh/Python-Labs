from math import pi

r1 = int(input("R1 = "))
print("R1 > R2")
r2 = int(input("R2 = "))
while r1 < r2:
    print("Неверный ввод, R1 > R2")
    r2 = int(input("R2 = "))
s1 = pi*(r1**2)
s2 = pi*(r2**2)
print("S1 =", s1)
print("S2 =", s2)
print("S3 =", s1-s2)