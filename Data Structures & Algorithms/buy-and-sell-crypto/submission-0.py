class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left= 0
        right= 1
        total=0
        while right < len(prices):
            curr=0
            if prices[right] > prices[left]:
                curr = prices[right] - prices[left]
            else:
                left= right
              
            
            if curr > total:
                total= curr
            right+=1
        return total