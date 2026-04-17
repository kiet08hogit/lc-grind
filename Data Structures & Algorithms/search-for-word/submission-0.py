class Solution:



    def dfs(self,board,r,c,index,word):
        row= len(board)
        cols= len(board[0])
        if index == len(word):
            return True
        if r < 0 or c <0 or r >=row or c>= cols or board[r][c] != word[index]:  
            return False

        temp = board[r][c]
        board[r][c] = "0"
        found= (
            self.dfs(board,r,c-1,index+1,word) or
            self.dfs(board,r,c+1,index+1,word) or
            self.dfs(board,r-1,c,index+1,word) or
            self.dfs(board,r+1,c,index+1,word)

        )
        
        board[r][c]=temp
        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return
        row= len(board)
        cols= len(board[0])
        index= 0
        for r in range(row): 
            for c in range(cols):
                if self.dfs(board,r,c,index,word):
                    return True
      
        return False