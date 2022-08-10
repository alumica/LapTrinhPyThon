# Tinh trung binh cong cua n so nguyen duong duoc nhap tu ban phim.
# Nhap sai 1 so (nhap so am) thoat truong trinh

n = int(input("Nhap n: "))
t = 0

for i in range(1, n+1):
    x = int(input("Nhap so nguyen duong {}: ".format(i)))
    if x < 0:
        print("Nhap sai, ket thuc chuong trinh")
        break
    else:
        t += x
    if i == (n):
        print("Trung binh cong: ", t/n)

