# Bai 15
n = int(input("Nhap n: "))
print("N la so le" if n//2==1 else "N la so chan")
if n//4==0:
    print("N chia het cho 4")
else:
    print("N khong chia het cho 4")
    if n//2==0:
        print("N chia het cho 2")
    else:
        print("N khong chia het cho 2")
m = int(input("Nhap so M: "))
print("N chia chan cho M" if n//m==0 else "N khong chia chan cho M")
# Bai 16 + mo rong
A = int(input("Nhap so tien A: "))
B = int(input("Nhap so tien B: "))
if A>B:
    print("Khach hang con thieu {}".format(A-B))
    exit()
elif A==B:
    print("Cam on khach hang. Hen gap lai !")
    exit()
elif A<B:
    tien = B-A
    print("Thoi lai {} cho khach hang" .format(tien))
    gia = 500
    tongTo = 0
    while tien > 0:
        soTo = tien // gia
        if soTo > 0:
            print("Loai {} gom {} to: ".format(int(gia), int(soTo)))
        tongTo += soTo
        tien -= soTo * gia
        gia /= 2
        if gia == 250:
            gia = 200
        if gia == 25:
            gia = 20
        if gia == 2.5:
            gia = 2
    print("Tong cong co {} to tien".format(int(tongTo)))
