# Tinh tong cac so le <= n, tru cac so chia het cho 3

n = int(input("Nhap n: "))
t = 0

for x in range(1, n+1, 2):
    t += x

for x in range(0, n+1):
    if (x % 3 == 0):
        t -= x

print(t)