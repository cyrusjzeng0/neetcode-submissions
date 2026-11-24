class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)] # initialize empty sets for each row, col and square; each is a set of nums in it
        for r in range(9): # rows
            for c in range(9): # cols
                n = board[r][c]
                if n == ".": continue
                square = (r//3) * 3 + (c//3)
                if n in rows[r] or n in cols[c] or n in squares[square]:
                    return False
                rows[r].add(n)
                cols[c].add(n)
                squares[square].add(n)
        
        return True
                
