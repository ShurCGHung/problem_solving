"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

def solution(s):
    sentence = []
    for char in s:
        if char.isupper():
            sentence.append(" ")
        sentence.append(char)
    return "".join(sentence)

if __name__ == "__main__":
    print(solution(s="breakCamelCase"))