"""
Largest Prime Factor
"""
import math
import time

def largestPrimeFactor(number: int) -> int:
    """Optimized solution"""
    largest_factor = 0

    # Handling even numbers
    while number % 2 == 0:
        largest_factor = 2
        number //= 2

    # Finding other prime factors
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            largest_factor = i
            number //= i

    # If the remaining number is a prime greater than 2
    if number > 2:
        largest_factor = number

    return largest_factor

if __name__ == "__main__":
    start_time = time.time()
    print(largestPrimeFactor(number=600851475143))
    print("--- %.10f seconds ---" % (time.time() - start_time))