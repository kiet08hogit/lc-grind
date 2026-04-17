class Solution:
    def __init__(self):
        self.memo = {}
    def fibo(self, n:int)->int:
        if n <= 1:
            return 1
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.fibo(n - 1) + self.fibo(n - 2)
        return self.memo[n]
    def climbStairs(self, n: int) -> int:
        result= 0   
        result += self.fibo(n)
        return result