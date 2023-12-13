"""
Longest Collatz Sequence in the limit range
"""
import time

def calEven(number: int) -> int:
    return number // 2 

def calOdd(number: int) -> int:
    return 3 * number + 1

def longest_collatz_sequence(limit: int) -> int:
    max = 0
    number = 0
    
    for i in range(limit // 2, limit):
        count = count_term_collatz_sequene(i)
        if (count > max):
            max = count
            number = i

    return number

def count_term_collatz_sequene(starting: int) -> int:
    count = 1
    
    while (starting != 1):
        count += 1
        if starting % 2 == 0:
            starting = calEven(number=starting)
        else:
            starting = calOdd(number=starting)
        
    return count

if __name__ == "__main__":
    start_time = time.time()
    print(longest_collatz_sequence(1000000))
    print(" --- %.10f seconds --- " % (time.time() - start_time))