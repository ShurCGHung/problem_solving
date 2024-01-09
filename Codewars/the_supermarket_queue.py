"""
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

Input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.

Output
The function should return an integer, the total time required.
"""

def queue_time(customers, n):
    if n == 1:
        return sum(customers)
    tills = [0] * n
    for c in customers:
        tills[0] += c
        tills.sort()
    return max(tills)

if __name__ == "__main__":
    queue_time(customers=[1, 2, 3, 4, 5], n=100)