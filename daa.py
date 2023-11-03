import tkinter as tk

class Solution:
    def __init__(self):
        self.board = [[None] * 9 for _ in range(9)]

    def helper(self, val, r, c):
        for i in range(9):
            if self.board[r][i] == val and i != c:
                return False
            if self.board[i][c] == val and i != r:
                return False
            if self.board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == val and r != (3 * (r // 3) + i // 3) and (3 * (c // 3) + i % 3) != c:
                return False
        return True

    def solveSudoku(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] is None:
                    for k in map(str, range(1, 10)):
                        if self.helper(k, i, j):
                            self.board[i][j] = k
                            if self.solveSudoku():
                                return True
                            self.board[i][j] = None
                    return False
        return True

def display_board(board):
    for row in board:
        print(' '.join(row))

def solve_puzzle():
    solver = Solution()
    for i in range(9):
        for j in range(9):
            value = entry_values[i][j].get()
            solver.board[i][j] = value if value != "" else None

    if solver.solveSudoku():
        display_board(solver.board)
        update_gui_board(solver.board)
    else:
        print("No solution found")

def update_gui_board(board):
    for i in range(9):
        for j in range(9):
            entry_values[i][j].set(board[i][j])

root = tk.Tk()
root.title("Sudoku Solver")

entry_values = [[tk.StringVar() for _ in range(9)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        entry = tk.Entry(root, textvariable=entry_values[i][j], width=18)
        entry.grid(row=i, column=j, padx=10,pady=10)

solve_button = tk.Button(root, text="Solve", command=solve_puzzle,  height=1, width=20)
solve_button.grid(row=9, columnspan=9)
root.geometry("1280x720")

root.mainloop()
