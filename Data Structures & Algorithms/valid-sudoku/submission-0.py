class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols= len(board[0])
        trackrows=defaultdict(set)
        trackcols=defaultdict(set)
        trackboxes=defaultdict(set)
        for r in range (rows):
            for c in range (cols):
                num= board[r][c]
                if num == ".":
                    continue
                boxidx= (r//3, c//3)
                if num in trackrows[r]:
                    return False
                if num in trackcols[c]:
                    return False
                if num in trackboxes[boxidx]:
                    return False
                else:
                    trackrows[r].add(num)
                    trackcols[c].add(num)
                    trackboxes[boxidx].add(num)
        return True

                