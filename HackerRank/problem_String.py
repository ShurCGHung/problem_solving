# Alphabet Rangoli

def print_rangoli(size):
    # your code goes here
    import string

    # Create a list of alphabets to use for the pattern
    alphabets = string.ascii_lowercase

    # Create the top part of the Rangoli
    for i in range(size-1, 0, -1):
        row = ['-'] * (2 * size - 1)
        for j in range(size - i):
            row[size - 1 - j] = alphabets[j + i]
            row[size - 1 + j] = alphabets[j + i]
        print('-'.join(row))

    # Create the center line of the Rangoli
    for i in range(0, size):
        row = ['-'] * (2 * size - 1)
        for j in range(0, size - i):
            row[size - 1 - j] = alphabets[j + i]
            row[size - 1 + j] = alphabets[j + i]
        print('-'.join(row))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)