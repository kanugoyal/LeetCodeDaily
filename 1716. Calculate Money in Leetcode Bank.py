class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        remaining_days = n % 7

        total_weeks = 28 * weeks + 7 * (weeks * (weeks - 1)) // 2
        total_remaining_days = (remaining_days * (remaining_days + 1)) // 2 + weeks * remaining_days

        return total_weeks + total_remaining_days