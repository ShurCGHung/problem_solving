"""
Difficulty: 5 kyu

Topic: Number of trailing zeros of N!

Summary:
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Be careful 1000! has 2568 digits...
"""
def zeros(n):
    if n <= -1:
        return 0
    count = 0
    while (n >= 5):
        n //= 5
        count += n
    return count

if __name__ == "__main__":
    print(zeros(n=12))