# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

# extra constraints
# make this with no extra memory: in place.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]


def rotate_matrix( matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """


    left = 0
    right = len(matrix[0]) - 1 # number of columns - 1 for index purposes

    top = 0
    bottom = len(matrix) - 1 # number of rows - 1 for index purposes

    while left < right:
        for i in range(right-left):
            # save the top left:
            top_left = matrix[top][left + i]

            # move bottom left into the top left
            matrix[top][left + i] = matrix[bottom - i][left]

            # move bottom right to the bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # move top right into the bottom right
            matrix[bottom][right - i] = matrix[top + i][right]

            # move top left into top right
            matrix[top + i][right] = top_left

        left += 1
        right -= 1

        top += 1
        bottom -= 1

def rotate_matrix_2(matrix: List[List[int]]) -> None:
    n = len(matrix)
    rotated_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n-i-1] = matrix[i][j]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = rotated_matrix[i][j]


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]

    