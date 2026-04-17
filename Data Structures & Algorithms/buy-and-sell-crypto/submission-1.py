class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r= 1
        maxval=0
        while r < len(prices):
            curr= 0
            if prices[l] > prices[r]:
                l=r
            else:
                curr= prices[r] - prices[l]
            if curr > maxval:
                maxval= curr
            r+=1
        return maxval