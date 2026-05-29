"""
Bài 2: Các hàm xử lý số nguyên tố (SNT).
Mã đề: 214
"""
import math

def is_prime(n):
    """Hàm bổ trợ kiểm tra một số có phải số nguyên tố hay không"""
    if n < 2:
        return False
    # Kiểm tra từ 2 đến căn bậc hai của n
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def cau_2a():
    """Yêu cầu a: Nhập n, kiểm tra n có phải số nguyên tố"""
    n = int(input("Nhập số nguyên dương n (Kiểm tra SNT): "))
    if is_prime(n):
        print(f"-> {n} là số nguyên tố.")
    else:
        print(f"-> {n} không phải là số nguyên tố.")

def cau_2b():
    """Yêu cầu b: Nhập n, đếm các số nguyên tố nhỏ hơn n"""
    n = int(input("Nhập số nguyên dương n (Đếm SNT < n): "))
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    print(f"-> Số lượng các số nguyên tố nhỏ hơn {n} là: {count}")

def cau_2c():
    """Yêu cầu c: Nhập n, liệt kê các ước số của n mà là số nguyên tố"""
    n = int(input("Nhập số nguyên dương n (Ước số là SNT): "))
    uoc_snt = []
    for i in range(1, n + 1):
        if n % i == 0 and is_prime(i):
            uoc_snt.append(i)
    
    # Chuyển kết quả thành chuỗi định dạng ngăn cách bằng dấu phẩy
    result_str = ",".join(map(str, uoc_snt))
    print(f"-> Các ước của {n} là số nguyên tố: {result_str}")

def main():
    print("--- CHƯƠNG TRÌNH XỬ LÝ SỐ NGUYÊN TỐ ---")
    cau_2a()
    print("-" * 30)
    cau_2b()
    print("-" * 30)
    cau_2c()

if __name__ == "__main__":
    main()
