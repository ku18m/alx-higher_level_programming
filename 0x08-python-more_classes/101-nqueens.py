#!/usr/bin/python3

"""
Solves the N queens problem.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""

import sys

if __name__ == "__main__":
    solutions = []
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)
    for i in range(n):
        solutions.append([i, None])

    def isqueen(y):
        """Check if it's a queen.
        Args:
            y: The position to check.
        """
        for x in range(n):
            if y == solutions[x][1]:
                return True
        return False

    def is_solution(x, y):
        """Checks if it's a solution or not.
        Args:
            x: The position to check.
            y: The position to check.
        """
        if (isqueen(y)):
            return False
        i = 0
        while(i < x):
            if abs(solutions[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def del_solution(x):
        """Deletes the wrong solutions.
        Args:
            x: The position to delete.
        """
        for i in range(x, n):
            solutions[i][1] = None

    def find_solution(x):
        """Finds the solution
        Args:
            x: The position to start.
        """
        for y in range(n):
            del_solution(x)
            if is_solution(x, y):
                solutions[x][1] = y
                if (x == n - 1):
                    print(solutions)
                else:
                    find_solution(x + 1)

    find_solution(0)
