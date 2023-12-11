# Print spiral 2d matrix into an array

def print_spiral(matrix, top, bottom, left, right):
    while left <= right and top <= bottom:

        # Print top row
        for i in range(left, right+1):
            print(matrix[top][i], end=' ')
        top += 1

        # Print right column
        for i in range(top, bottom+1):
            print(matrix[i][right], end=' ')
        right -= 1

        # Print bottom row
        if top <= bottom:
            for i in range(right, left-1, -1):
                print(matrix[bottom][i], end=' ')
            bottom -= 1

        # Print left column
        if left <= right:
            for i in range(bottom, top-1, -1):
                print(matrix[i][left], end=' ')
            left += 1


# Test the function
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

print_spiral(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1)