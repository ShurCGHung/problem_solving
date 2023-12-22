"""
Digital root is recursive sum of all digits in a number

Given n, take the sum of all digits of n. If that value has more than one digit, continue reducing in this way untila single-digit number is produced, the input will be a non-negative number

16 --> 1 + 6 = 7
942 --> 9 + 4 + 2 = 14 --> 1 + 4 = 5

Solve it in O(1) space
"""
import time

def calculateDigitalRoot(number: str) -> int:
    if number == "0":
        return 0
    else:
        ans = 0
        for i in range(0, len(number)):
            ans += int(number[i])
            ans %= 9
    return 9 if ans % 9 == 0 else ans % 9

def calculateDigitalRoot2(number: str) -> int:
    numb = int(number)
    numb -= 1
    return (numb % 9) + 1

if __name__ == "__main__":
    number = "65785412124661581210412565153168151512316516151"
    start_time = time.time()
    print(calculateDigitalRoot(number=number))
    print(" --- %.10f seconds --- " % (time.time() - start_time))
    
    
    start_time = time.time()
    print(calculateDigitalRoot2(number=number))
    print(" --- %.10f seconds --- " % (time.time() - start_time))