"""Largest palindrome product for two 3-digit numbers """

def isPalindrome(s: int) -> bool:
    return str(s) == str(s)[::-1]

def largestPalindromeProduct() -> int:
    largestPalindromeProduct = 0 

    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j

            if isPalindrome(product) and product > largestPalindromeProduct:
                largestPalindromeProduct = product

    return largestPalindromeProduct

if __name__ == "__main__":
    result = largestPalindromeProduct()
    print("The largest palindrome made from the product of two 3-digit numbers is:", result)