"""Constant representing an empty square"""
EMPTY = " "

""" 
-List of all 8 possible winning lines
- First 3 lines -- rows (top, middle, bottom)
- Next 3 lines  -- columns (left, middle, right)
- Last 2 lines  -- diagonals (top-left to bottom-right, top-right to bottom-left)
"""
WINS = [
    [(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)],
    [(0,0),(1,0),(2,0)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)],
    [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)],
]

"""Represents the 3x3 Tic-Tac-Toe grid """
class Board:
    def __init__(self):
        self.grid = []
        """this will loop 3 times and assign each one to empty (EMPTY=" ") """
        for i in range(3):
            self.grid.append([EMPTY, EMPTY, EMPTY])
    """ Returns the value at flat index i (0-8) """
    def get(self, i):
        return self.grid[i//3][i%3]

    """Places symbol ("X" or "O") at index i """
    def set(self, i, symbol):
        self.grid[i//3][i%3] = symbol

    """Check if i is between 0 and 8 and if self.get(i) is empty"""
    def is_valid(self, i):
        return 0 <= i <= 8 and self.get(i) == EMPTY

    """Checks all 8 winning lines and returns the winner's symbol or None"""
    def winner(self):
        for (row_1, col_1), (row_2, col_2), (row_3, col_3) in WINS:
            cell_1 = self.grid[row_1][col_1]
            cell_2 = self.grid[row_2][col_2]
            cell_3 = self.grid[row_3][col_3]

            if cell_1 == cell_2 == cell_3 != EMPTY:
                return cell_1
        return None

    """Check if every space is occupied or not"""
    def full(self):
        return EMPTY not in [cell for row in self.grid for cell in row]

    """display the current state of the board"""
    def display(self):
        for r in range(3):
            print(" | ".join(self.grid[r]))
            if r < 2:
                print("---------")