class Solution:
    def helper(self, arr: list) -> int:
        total= 0 
        for num in arr:
            total+= num ** 2
        return total
    def isHappy(self, n: int) -> bool:
        digits = [int(x) for x in str(n)]
        s = set()
        while True:
            sumofnum= self.helper(digits)
            digits = [int(x) for x in str(sumofnum)]
            if sumofnum in s:
                return False
            s.add(sumofnum)
            if sumofnum == 1:
                return True
        
        return False
