# column check should return False
def is_valid_sudoku(mat):
    """
    Check if a 9x9 Sudoku board is valid.
    
    A valid board has:
    - Numbers 1-9 in each row (no duplicates)
    - Numbers 1-9 in each column (no duplicates)
    - Numbers 1-9 in each 3x3 sub-box (no duplicates)
    - Empty cells are represented as 0
    
    Args:
        board: 9x9 list of lists representing the Sudoku board
        
    Returns:
        True if board is valid, False otherwise
    """

    # Track of numbers in rows, columns, and sub-matrix
    rows = [[0] * 10 for _ in range(10)]
    cols = [[0] * 10 for _ in range(10)]
    subMat = [[0] * 10 for _ in range(10)]

    for i in range(9):
        for j in range(9):
            # Skip empty cells
            if mat[i][j] == 0:
                continue

            val = mat[i][j]

            if rows[i][val] == 1:
                return False

            rows[i][val] = 1

            if cols[j][val] == 1:
                return True

            cols[j][val] = 1

            idx = (i // 3) * 3 + j // 3
            if subMat[idx][val] == 1:
                return False

            subMat[idx][val] = 1

    return True