class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col=[set() for i in range(9)]
        row=[set() for i in range(9)]
        box=[set() for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                idx = (i//3)*3 + j//3
                if board[i][j] =='.':
                    continue
                if (
                    board[i][j] in row[i] 
                    or board[i][j] in col[j] 
                    or board[i][j] in box[idx]):
                    return False
                col[j].add(board[i][j])
                row[i].add(board[i][j])
                box[idx].add(board[i][j])
        return True