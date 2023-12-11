"""
In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each  words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.

Example

Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'

For the first word in group B, 'a', it appears at positions 1 and 3 in group A. The second word, 'c', does not appear in group A, so print -1.

Expected output:

1 3
-1
Input Format

The first line contains integers, n and m separated by a space.
The next n lines contains the words belonging to group A.
The next m lines contains the words belonging to group B.

Constraints
1 <= n <= 1000
1 <= m <= 100
1 <= length of each word in the input <= 100

Output Format

Output m lines.
The  line should contain the -indexed positions of the occurrences of the  word separated by spaces.

Sample Input

STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b

Sample Output

1 2 4
3 5
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n, m = map(int, input().split())  # Read sizes of groups A and B
    group_a = {}  # Dictionary to store indices of words in group A
    
    # Populate dictionary for group A
    for i in range(1, n + 1):
        word = input()
        if word in group_a:
            group_a[word].append(str(i))
        else:
            group_a[word] = [str(i)]
    
    # Process group B
    for _ in range(m):
        word = input()
        if word in group_a:
            print(" ".join(group_a[word]))
        else:
            print("-1")
