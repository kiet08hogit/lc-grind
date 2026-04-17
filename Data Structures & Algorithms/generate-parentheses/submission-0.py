class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        temp=[]
        def backtracking(openbr,closebr):
            if openbr== closebr== n:
                ans.append(''.join(temp))
                return 
            if openbr < n:
                temp.append("(")
                backtracking(openbr+1,closebr)
                temp.pop()
            if closebr < openbr:
                temp.append(")")
                backtracking(openbr,closebr+1)
                temp.pop()
        backtracking(0,0)
        return ans