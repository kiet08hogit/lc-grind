class Solution:
    def reverse(self, x: int) -> int:
        sign = None
        if x < 0:
            sign = -1
        else: 
            sign = 1
        ans= sign * (int(str(abs(x))[::-1]))
        if ans > 2**31 - 1 or ans < -2**31:
            return 0
        return ans