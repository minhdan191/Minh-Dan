# San loc so nguyen to
# is_prime[i] = True neu i la so nguyen to

LIMIT = 1_000_000
is_prime = [False, False] + [True] * (LIMIT - 1)
i = 2
while i * i <= LIMIT:
    if is_prime[i]:
        for j in range(i * i, LIMIT + 1, i):
            is_prime[j] = False
    i += 1

# bang xoay 180
STANDARD = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
EXTENDED = {**STANDARD, '2': '2', '5': '5'}

# kiem tra strobogrammatic
# xoay 180 do = dao chuoi * mang tung chu so -> phai ra chinh no
def is_strobo(n, ext=False):
    s = str(n)
    mp = EXTENDED if ext else STANDARD
    left, right = 0, len(s) - 1
    while left <= right:
        if s[left] not in mp or mp[s[left]] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def strobogrammatic(n):
    # Hàm xử lý phần a: Tìm số Pure Strobogrammatic
    result = []
    start = 10**(n-1) if n > 1 else 0
    end = 10**n
    for num in range(start, end):
        if is_strobo(num, ext=False):
            result.append(num)
    return result

def extended_strobogrammatic(n):
    # Hàm xử lý phần b: Tìm số Extended Strobogrammatic kèm điều kiện số nguyên tố
    result = []
    start = 10**(n-1) if n > 1 else 0
    end = 10**n
    for num in range(start, end):
        if is_strobo(num, ext=True) and is_prime[num]:
            result.append(num)
    return result

def print_results(title, results):
    print(f"{title}: {results}")

def main():
    try:
        n = int(input("Enter n (2 <= n <= 10): "))
        if not (2 <= n <= 10):
            raise ValueError
    except ValueError:
        print("Invalid input. n must be an integer between 2 and 10.")
        return

    part_a = strobogrammatic(n)
    print_results(f"Part a - Pure Strobogrammatic ({n} digits)", part_a)
    
    part_b = extended_strobogrammatic(n)
    print_results(f"Part b - Extended Strobogrammatic ({n} digits)", part_b)

if __name__ == "__main__":
    main()
