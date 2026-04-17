class Solution:
    def fibo(self, n:int)->int:
        if n <= 1:
            return 1
        return self.fibo(n-2) + self.fibo(n-1)
    def climbStairs(self, n: int) -> int:
        result= 0   

        result += self.fibo(n)
        return result