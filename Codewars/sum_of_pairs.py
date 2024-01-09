"""
Difficulty: 5 kyu

Topic: Sum of 

Summary:
Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

If there are two or more pairs with the required sum, the pair whose second element has the smallest index is the solution.
"""
def sum_pairs(ints, s):
    seen = {}
    
    for num in ints:
        complement = s - num
        if complement in seen:
            return [complement, num]
        seen[num] = True
    
    return None