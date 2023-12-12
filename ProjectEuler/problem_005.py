import math

def smallestMultiple() -> int:
    total = 1

    for i in range(1, 21):
        total = (total * i) // math.gcd(total, i)

    return total

if __name__ == "__main__":
    print(smallestMultiple())

"""
i = 1 => total = (1 * 1) // 1
i = 2 => total = (1 * 2) // 1
i = 3 => total = (1 * 3) // 1
i = 4 => total = (1 * 4) // 1
"""