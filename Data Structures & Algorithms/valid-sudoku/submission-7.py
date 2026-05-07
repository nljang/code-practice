class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for char in row:
                if char == '.':
                    continue
                if char in seen:
                    return False
                seen.add(char)
        
        for i in range(9):
            seen = set()
            for row in board:
                if row[i] == '.':
                    continue                
                if row[i] in seen:
                    return False
                seen.add(row[i])
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for x in range(3):
                    for y in range(3):
                        char = board[i + x][j + y]
                        if char == '.':
                            continue
                        if char in seen:
                            return False
                        seen.add(char)
        
        return True
