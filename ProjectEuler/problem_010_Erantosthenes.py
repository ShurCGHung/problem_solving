"""
Problem 10 - Optimized:

Using Sieve of Erantosthenes to pfind prime number
=> Sum of all primes below limit
"""
import time
import math

def sieve_of_Erantosthenes(limit: int) -> int:
    sum = 0

    crosslimit = math.floor(math.sqrt(limit)) # Calculate the square root of the limit, get the floor integer

    sieve = [False] * (limit + 1) # Create a boolean array initialized to False

    # Mark even numbers greater than 2 as True
    for number in range(4, limit + 1, 2):
        sieve[number] = True

    # Sieve of Erantosthenes algorithm
    for number in range(3, crosslimit + 1, 2):
        if not sieve[number]: # If number is not marked, it's a prime number
            for m in range(number * number, limit + 1, 2 * number):
                sieve[m] = True

    for number in range(2, limit + 1):
        if not sieve[number]:
            sum += number

    return sum

if __name__ == "__main__":
    start_time = time.time()
    print(sieve_of_Erantosthenes(limit=20000000))
    print(" --- %.10f seconds --- " % (time.time() - start_time))