"""
Summation of all primes below threshold
"""

import math, time

def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True

    # Check for divisibility by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check for divisibility by numbers of the form 6k ± 1
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True

def sumOfPrime(number: int) -> int:
    total = 0

    for each in range (1, number + 1):
        if (isPrime(each)):
            total += each

    return total

if __name__ == "__main__":
    start_time = time.time()
    print(sumOfPrime(number=20000000))
    print(" --- %.10f seconds --- " % (time.time() - start_time))