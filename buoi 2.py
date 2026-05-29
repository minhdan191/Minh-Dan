dai = float(input("Nhập chiều dài đáy hình chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))
so_le = int(input("Số lượng số lẻ cần hiển thị: "))

dien_tich_day = dai * rong
the_tich = dien_tich_day * cao

print(f"Diện tích đáy hình chữ nhật = {dien_tich_day:.{so_le}f}cm²")
print(f"Thể tích hình khối= {the_tich:.{so_le}f}cm³")
#bai 5
n = int(input("Nhập số nguyên dương n: "))

tong = 0
tich = 1

temp = n  # giữ lại n ban đầu

while temp > 0:
    digit = temp % 10
    tong += digit
    tich *= digit
    temp //= 10

print("Tổng =", tong)
print("Tích =", tich)

#bai 6
n = int(input("Nhập số nguyên dương n: "))

max_digit = 0
temp = n

while temp > 0:
    digit = temp % 10
    if digit > max_digit:
        max_digit = digit
    temp //= 10

print("Số lớn nhất =", max_digit)

# bai 7
n = int(input("Nhập số nguyên dương n: "))

temp = n
is_lucky = True

while temp > 0:
    digit = temp % 10
    if digit != 6 and digit != 8:
        is_lucky = False
        break
    temp //= 10

if is_lucky:
    print(n, "là số may mắn")
else:
    print(n, "KHÔNG phải số may mắn")
