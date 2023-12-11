"""If we list all natural number below 10 that are mutliplies of 3 or 5, we get 3, 5, 6, 9. The sum of these multiplies is 23

Finish the solution so that it returns the sum of all multiplies of 3 or 5 **below** the number passed in.

Additionally, if the number is negative, return 0.

Note: if the number is a multiplies of **both** 3 and 5, only count it once.
"""
import time

def sum_of_all_requirements(n: int) -> int:

    # Original solution O(n)
    # total = 0
    
    # for i in range(1, n):
    #     if (i % 3 == 0 or i % 5 == 0):
    #         total += i
    
    # Optimized solution O(1)
    d3 = (n - 1) // 3
    d5 = (n - 1) // 5
    d15 = (n - 1) // 15
    return (3 + d3 * 3) * d3 / 2 + (5 + d5 * 5) * d5 / 2 - (15 + d15 * 15) * d15 / 2

    # return total

if __name__ == "__main__":
    start_time = time.time()
    print(sum_of_all_requirements(1000))
    print("--- %.10f seconds ---" % (time.time() - start_time))