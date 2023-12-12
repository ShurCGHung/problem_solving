"""
Pythagoras triplet
"""

import time
def productTriplet(number: int) -> int:
    for a in range(1, number):
        for b in range(1, number):
            c = number - a - b
            if a * a + b * b == c * c:
                print("{} {} {}".format(a, b, c))
                return a * b * c

if __name__ == "__main__":
    start_time = time.time()
    print(productTriplet(number=100000))
    print(" --- %.10f seconds --- " % (time.time() - start_time))