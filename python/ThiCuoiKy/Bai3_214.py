"""
Bài 3: Kiểm tra số chính phương và phân loại tam giác.
Mã đề: 214
"""
import math

def is_perfect_square(n):
    """Hàm nhận vào 1 đối số n, kiểm tra xem n có phải số chính phương"""
    if n < 0:
        return False
    root = math.isqrt(n)
    return root * root == n

def classify_triangle(a, b, c):
    """Hàm nhận vào 3 tham số, kiểm tra điều kiện tam giác và phân loại"""
    # Điều kiện hình thành một tam giác (Tổng 2 cạnh lớn hơn cạnh còn lại)
    if a + b > c and a + c > b and b + c > a:
        # Kiểm tra tam giác đều
        if a == b == c:
            return "Tam giác đều"
        
        # Kiểm tra các trường hợp tam giác cân hoặc vuông cân
        elif a == b or b == c or a == c:
            # Điều kiện định lý Pitago cho tam giác vuông
            if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
                return "Tam giác vuông cân"
            return "Tam giác cân"
        
        # Kiểm tra tam giác vuông thường
        elif (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
            return "Tam giác vuông"
        
        # Trường hợp còn lại
        else:
            return "Tam giác thường"
    else:
        return "Không phải là 3 cạnh hợp lệ của 1 tam giác"

def main():
    print("--- KIỂM TRA SỐ CHÍNH PHƯƠNG & TAM GIÁC ---")
    # Thử nghiệm hàm số chính phương
    n_cp = int(input("Nhập số nguyên n cần kiểm tra số chính phương: "))
    if is_perfect_square(n_cp):
        print(f"-> {n_cp} LÀ số chính phương.")
    else:
        print(f"-> {n_cp} KHÔNG PHẢI số chính phương.")
        
    print("-" * 30)
    # Thử nghiệm hàm phân loại tam giác
    print("Nhập vào 3 số nguyên là độ dài 3 cạnh:")
    a = int(input("Cạnh a = "))
    b = int(input("Cạnh b = "))
    c = int(input("Cạnh c = "))
    ket_qua_tam_giac = classify_triangle(a, b, c)
    print(f"-> Kết quả phân loại: {ket_qua_tam_giac}")

if __name__ == "__main__":
    main()
