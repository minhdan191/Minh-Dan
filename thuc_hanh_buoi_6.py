# ==========================================
# 1. ĐỊNH NGHĨA CÁC HÀM LAMBDA / HÀM THEO YÊU CẦU
# ==========================================

# e) Số phong phú
is_abundant = lambda n: sum(i for i in range(1, n) if n % i == 0) > n

# f) Số tăng dần
is_increasing = lambda n: all(str(n)[i] <= str(n)[i+1] for i in range(len(str(n)) - 1))

# g) Số Armstrong
is_armstrong = lambda n: sum(int(d) ** len(str(n)) for d in str(n)) == n

# h) Số nguyên tố
is_prime_c1 = lambda n: len([i for i in range(1, n + 1) if n % i == 0]) == 2
is_prime_c2 = lambda n: sum(i for i in range(1, n + 1) if n % i == 0) == n + 1
is_prime_c3 = lambda n: n > 1 and not any(n % i == 0 for i in range(2, int(n**0.5) + 1))

def F(k):
    if k <= 1: return False
    return len(list(filter(lambda x: k % x == 0, range(2, k)))) == 0

# i) Số Palindrome
is_palindrome = lambda n: str(n) == str(n)[::-1]

# j) Số nguyên tố Palindrome
is_prime_palindrome = lambda n: (n > 1 and not any(n % i == 0 for i in range(2, int(n**0.5) + 1))) and (str(n) == str(n)[::-1])

# k) Số lộc phát
is_loc_phat_c1 = lambda n: all(d in '68' for d in str(n))
is_loc_phat_c2 = lambda n: str(n).count('6') + str(n).count('8') == len(str(n))

# l) Số lộc phát Palindrome
is_loc_phat_palindrome = lambda n: all(d in '68' for d in str(n)) and (str(n) == str(n)[::-1])


# ==========================================
# 2. CHƯƠNG TRÌNH IN KẾT QUẢ TRONG KHOẢNG 1 ĐẾN 1 TRIỆU
# ==========================================

CHAN_TREN = 1000000

print("--- KẾT QUẢ KIỂM TRA TỪ 1 ĐẾN 1,000,000 ---")

# f) Số tăng dần
print("\n> Các số tăng dần (In demo 20 số đầu):")
increasing_nums = [x for x in range(1, CHAN_TREN + 1) if is_increasing(x)]
print(f"Tổng số lượng: {len(increasing_nums)}. 20 số đầu: {increasing_nums[:20]}")

# g) Số Armstrong
print("\n> Các số Armstrong:")
armstrong_nums = [x for x in range(1, CHAN_TREN + 1) if is_armstrong(x)]
print(armstrong_nums)

# h) Số nguyên tố (Sử dụng cách 3 để tối ưu tốc độ)
print("\n> Các số nguyên tố (In demo 20 số đầu):")
prime_nums = [x for x in range(1, CHAN_TREN + 1) if is_prime_c3(x)]
print(f"Tổng số lượng: {len(prime_nums)}. 20 số đầu: {prime_nums[:20]}")

# i) Số Palindrome
print("\n> Các số Palindrome (In demo 20 số đầu):")
palindrome_nums = [x for x in range(1, CHAN_TREN + 1) if is_palindrome(x)]
print(f"Tổng số lượng: {len(palindrome_nums)}. 20 số đầu: {palindrome_nums[:20]}")

# j) Số nguyên tố Palindrome
print("\n> Các số nguyên tố Palindrome:")
prime_palindrome_nums = [x for x in range(1, CHAN_TREN + 1) if is_prime_palindrome(x)]
print(prime_palindrome_nums)

# k) Số lộc phát
print("\n> Các số lộc phát:")
loc_phat_nums = [x for x in range(1, CHAN_TREN + 1) if is_loc_phat_c1(x)]
print(f"Tổng số lượng: {len(loc_phat_nums)}. Chi tiết: {loc_phat_nums}")

# l) Số lộc phát Palindrome
print("\n> Các số lộc phát Palindrome:")
loc_phat_palindrome_nums = [x for x in range(1, CHAN_TREN + 1) if is_loc_phat_palindrome(x)]
print(loc_phat_palindrome_nums)

# e) Số phong phú (Chạy thuật toán kiểm tra ước số đến 1 triệu rất nặng, demo đến 10,000)
print("\n> Các số phong phú (Demo trong khoảng 1 đến 10,000):")
abundant_nums = [x for x in range(1, 10001) if is_abundant(x)]
print(f"20 số đầu tiên: {abundant_nums[:20]}")
