class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first_min = float('inf')
        second_min = float('inf')
        for i in range(len(prices)):
            if prices[i] <= first_min:
                first_min,second_min = prices[i],first_min
            elif prices[i]<second_min:
                second_min = prices[i]
        left = money - first_min - second_min
        if left>=0:
            return left
        return money 