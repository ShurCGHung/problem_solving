"""
Highly divisible triangular number
"""
def count_divisors(number: int) -> int:
    count = 0
    sqrt_num = int(number ** 0.5) + 1
    for i in range(1, sqrt_num):
        if number % i == 0:
            count += 2
    if sqrt_num ** 2 == number:
        count -= 1
    
    return count

def findTriangularNumber(divisors: int) -> int:
    n = 1
    while True:
        triangle_number = n * (n + 1) // 2
        div_count = count_divisors(triangle_number)
        if div_count > divisors:
            return triangle_number
        n += 1

if __name__ == "__main__":
    print(findTriangularNumber(divisors=500))