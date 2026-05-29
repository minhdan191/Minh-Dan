def solve_110():
    cipher_text = input("Nhập chuỗi nén: ")
    plain_text = ""
    i = 0
    while i < len(cipher_text):
        if cipher_text[i] == '#':
            # Lấy số lượng (kí tự tiếp theo) và kí tự cần lặp
            count = int(cipher_text[i+1])
            char = cipher_text[i+2]
            plain_text += char * count
            i += 3 # Nhảy qua cụm #nc
        else:
            plain_text += cipher_text[i]
            i += 1
    print(f"Kết quả: {plain_text}")

# solve_110()
import math


def reverse_number(n):
    return int(str(n)[::-1])


def solve_114():
    try:
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))

        friendly_numbers = []
        for i in range(a, b + 1):
            rev_i = reverse_number(i)
            # Kiểm tra ƯCLN của i và số đảo ngược của nó
            if math.gcd(i, rev_i) == 1:
                friendly_numbers.append(i)

        print("Các số thân thiện:", *friendly_numbers)
        print(f"Số lượng: {len(friendly_numbers)}")
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ.")

# solve_114()
import math


def reverse_number(n):
    return int(str(n)[::-1])


def solve_114():
    try:
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))

        friendly_numbers = []
        for i in range(a, b + 1):
            rev_i = reverse_number(i)
            # Kiểm tra ƯCLN của i và số đảo ngược của nó
            if math.gcd(i, rev_i) == 1:
                friendly_numbers.append(i)

        print("Các số thân thiện:", *friendly_numbers)
        print(f"Số lượng: {len(friendly_numbers)}")
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ.")

# solve_114()
