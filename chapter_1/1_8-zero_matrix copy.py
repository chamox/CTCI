# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0



def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    
    # first, we are going to check if the first row of the matrix is going to be 0
    rows = len(matrix)
    cols = len(matrix[0])

    is_first_row_zero = False

    # determine wich rows and columns needs to be 0
    for r in range(rows):
        for c in range(cols):
            # if 0 found
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r>0:
                    matrix[r][0] = 0
                else:
                    is_first_row_zero = True
    # now we modify the matrix
    for r in range(1,rows):
        for c in range(1,cols):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    
    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] = 0

    if is_first_row_zero:
        for c in range(cols):
                matrix[0][c] = 0


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]

    