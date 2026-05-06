class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      
        for row in board:
            check_row = set()
            for char in row:
                if char != '.':
                    if char in check_row:
                        return False
                    else:
                        check_row.add(char)
        

        for i in range(9):
            check_column = set()
            for row in board:
                if row[i] != '.':
                    if row[i] in check_column:
                        return False
                    else:
                        check_column.add(row[i])
        
        
        for i in range(0, 9, 3):        
            for j in range(0, 9, 3):    #goes to top left for each 3x3
                check_box = set()
                for k in range(3):    #for three rows:
                    for l in range(3):    #take first 3 values
                        char = board[i + k][j + l]
                        if char != '.':
                            if char in check_box:
                                return False
                            else:
                                check_box.add(char)
        
        return True


