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

def get10001stPrimeNumber():
    count = 0

    result = 0
    index = 1

    while (count <= 10001):
        if (isPrime(index)):
            count += 1
            if (count == 10001):
                result = index
        index += 1    

    return result

if __name__ == "__main__":
    start_time = time.time()
    print(get10001stPrimeNumber())
    print("--- %.10f seconds ---" % (time.time() - start_time))