class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        first_max = 0
        second_max = 0
        first_min = float('inf')
        second_min = float('inf')


        for i in range(len(nums)):
            if nums[i] >= first_max:
                first_max,second_max = nums[i],first_max
            elif nums[i]>second_max:
                second_max = nums[i]
            if nums[i] <= first_min:
                first_min,second_min = nums[i],first_min
            elif nums[i]<second_min:
                second_min = nums[i]


        return (first_max*second_max)-(first_min*second_min)