def calculaterDifference(number: int) -> int:
    two_hat_each = (number * (number + 1) * (2 * number + 1)) / 6 # 1 ^ 2 + 2 ^ 2 + ... + n ^ 2 = (n * (n + 1) * (2n + 1)) / 6
    two_hat_sum = (number * (number + 1) / 2) # (1 + 2 + 3 + ... + n) ^ 2 = ((n * (n + 1)) / 2) ^ 2

    return int(two_hat_sum * two_hat_sum - two_hat_each)
    
    """Original solution"""
    limit = 100
    sum = 0
    sum_sq = 0
    for i in range(1, 101):
        sum += i
        sum_sq += (i * i)
    
    return (sum * sum) - sum_sq

if __name__ == "__main__":
    print(calculaterDifference(number=100))