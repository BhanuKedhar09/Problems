#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        if not nums:
            return 0
        n = len(nums)
        for i in range(n-1):
            if nums[i] != nums[i+1]:
                
                nums[index] = nums[i+1]
                
                index += 1
        return index