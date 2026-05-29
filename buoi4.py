# a) Trị tuyệt đối
abs_lambda = lambda n: abs(n)

# b) n + 15
add_15 = lambda n: n + 15

# c) tích x * y
multiply = lambda x, y: x * y

# d) kiểm tra bội của 13 hoặc 19
is_multiple_13_19 = lambda n: n % 13 == 0 or n % 19 == 0

# e) diện tích hình tròn (πr^2)
import math
circle_area = lambda r: math.pi * r * r

# f) chu vi hình chữ nhật (2 * (d + r))
rectangle_perimeter = lambda d, r: 2 * (d + r)

# g) kiểm tra số chính phương
is_perfect_square = lambda n: int(n * 0.5) * 2 == n

# h) kiểm tra số nguyên tố
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

# i) kiểm tra tam giác + phân loại
triangle_type = lambda a, b, c: (
    "Không phải tam giác" if a + b <= c or a + c <= b or b + c <= a
    else "Tam giác đều" if a == b == c
    else "Tam giác vuông" if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a
    else "Tam giác cân" if a == b or b == c or a == c
    else "Tam giác thường"
)
def factorial(n):
    """
    n! = n * (n-1)!
    """

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# Test
print(factorial(5))  # 120
def power(a, b):
    """
    Tính a^b bằng đệ quy
    """

    if b == 0:
        return 1

    return a * power(a, b - 1)


# Test
print(power(2, 3))  # 8
def gcd(a, b):
    """
    Thuật toán Euclid (đệ quy)
    gcd(a, b) = gcd(b, a % b)
    """

    if b == 0:
        return a

    return gcd(b, a % b)


# Test
print(gcd(12, 18))  # 6
def fibonacci(n):
    """
    Fibonacci theo đề:
    F0 = F1 = 1
    """

    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


# Test
print(fibonacci(7))  # 13
