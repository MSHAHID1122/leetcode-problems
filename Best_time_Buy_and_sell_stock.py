class Solution(object):
    def maxProfit(self, prices):
        left =0
        right = 1
        profit = 0
        while right <len(prices):
            if (prices[right]-prices[left])> profit:
                profit = prices[right]-prices[left]
            elif prices[right]<prices[left]:
                left =right
            right +=1

        return profit     