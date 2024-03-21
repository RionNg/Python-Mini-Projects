"""
Sudoku Solver
"""

board = [
    [0, 0, 5, 3, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 7, 0, 0, 1, 0, 5, 0, 0],
    [4, 0, 0, 0, 0, 5, 3, 0, 0],
    [0, 1, 0, 0, 7, 0, 0, 0, 6],
    [0, 0, 3, 2, 0, 0, 0, 8, 0],
    [0, 6, 0, 5, 0, 0, 0, 0, 9],
    [0, 0, 4, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 9, 7, 0, 0],
]


def is_valid_move(row, col, number):
    """
    Check if placing a number in a specific row and column of the board is valid.

    Parameters:
    - board (list of lists): The Sudoku board.
    - row (int): The row index.
    - col (int): The column index.
    - number (int): The number to be placed.

    Returns:
    - bool: True if the move is valid, False otherwise.
    """

    for x in range(9):
        if board[row][x] == number:
            return False

    for x in range(9):
        if board[x][col] == number:
            return False

    corner_row = row - row % 3
    corner_col = col - col % 3

    for x in range(3):
        for y in range(3):
            if board[corner_row + x][corner_col + y] == number:
                return False

    return True


def solve(row, col):
    """
    Solve the Sudoku puzzle recursively using backtracking.

    Parameters:
    - board (list of lists): The Sudoku board.
    - row (int): The current row index.
    - col (int): The current column index.

    Returns:
    - bool: True if a solution is found, False otherwise.
    """

    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if board[row][col] > 0:
        return solve(row, col + 1)

    for num in range(1, 10):

        if is_valid_move(row, col, num):

            board[row][col] = num

            if solve(row, col + 1):
                return True

        board[row][col] = 0

    return False


def print_board(bo):
    """
    Print the Sudoku board in a human-readable format.

    Parameters:
    - bo (list of lists): The Sudoku board to be printed.
    """

    for i, row in enumerate(bo):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")

        for j, cell in enumerate(row):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(cell, end="\n")
            else:
                print(str(cell) + " ", end="")


if solve(0, 0):
    print_board(board)
else:
    print("No solution for this Sudoku.")
