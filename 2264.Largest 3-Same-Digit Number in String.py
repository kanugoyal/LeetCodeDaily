class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if not max_good or int(num[i:i+3]) > int(max_good):
                    max_good = num[i:i+3]
        return max_good