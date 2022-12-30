#https://leetcode.com/problems/maximum-subarray/description/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #O(N^2)
        # sum_array = []
        # max_sum = float("-inf")
        # for i in range(len(nums)):
        #     sum =0
        #     for j in range(i, len(nums)):
        #         sum =sum +nums[j]
        #         max_sum = max(max_sum, sum)
        # # print(sum_array)
        # return max_sum

        maxi = nums[0]
        sum = 0
        for i in range(len(nums)):
            sum = sum+nums[i]
            maxi = max(sum, maxi)
            if sum < 0:
                sum = 0
        return maxi
